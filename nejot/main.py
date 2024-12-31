import os
import pymysql
import base64
import openai
import streamlit as st
from dotenv import load_dotenv

from streamlit_tags import st_tags
from streamlit_modal import Modal

from config import DB_CONFIG
from graphs.blog_generation_graph import blog_generation_workflow
from utils.ai_utils import get_ai_suggested_titles

import requests

# BACKEND_URL = "https://backdocsend.jamesmoon.click/blog/add"

# .env 파일 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # .env에 담긴 OPENAI_API_KEY 사용

st.set_page_config(layout="wide")

# 블로그 제목 입력과 AI 추천 제목 관련 상태 관리
if "blog_title_input" not in st.session_state:
    st.session_state["blog_title_input"] = ""
if "suggested_titles" not in st.session_state:
    st.session_state["suggested_titles"] = []
    

# 모달 객체 생성 (AI 추천 제목 목록을 표시하는 데 사용)
ai_titles_modal = Modal(
    "AI 추천 블로그 제목",  # 첫 번째 인자는 title
    key="ai_titles_modal"  # 두 번째 인자는 key
)

def regenerate_titles_cb():
    """콜백: GPT를 통해 새 제목 리스트를 세션에 저장 (재생성)"""
    product_name = st.session_state.get("product_name","")
    if not product_name:
        st.warning("제품명을 먼저 입력해주세요.")
        return
    new_titles = get_ai_suggested_titles(product_name, max_suggestions=4)
    if new_titles:
        st.session_state["suggested_titles"] = new_titles
    else:
        st.warning("추천 제목을 생성하지 못했습니다.")
    # rerun 없이도 streamlit이 한번 더 UI갱신 해주므로, 굳이 experimental_rerun 안써도 됨

def on_use_title_cb(selected: str):
    """사용하기 버튼 콜백: 라디오로 선택한 제목을 텍스트 입력 위젯에 반영"""
    if not selected:
        st.warning("제목을 선택하세요.")
        return
    # 여기서 위젯 key("blog_title_widget")에 해당하는 세션 값을 대입
    st.session_state["blog_title_widget"] = selected
    ai_titles_modal.close()

def close_modal_cb():
    """콜백: 모달 닫기"""
    ai_titles_modal.close()

left_col, right_col = st.columns([1,2])

with left_col:
    st.title("🦊에디's 블로그 글")

        # 제품명 저장을 위해 세션에 product_name 키 사용
    if "product_name" not in st.session_state:
        st.session_state["product_name"] = ""
    st.session_state["product_name"] = st.text_input("제품명을 입력하세요:", value=st.session_state["product_name"])

        # blog_title_input 키 사용 → AI가 선택한 제목을 반영 가능
    blog_title = st.text_input(
        "블로그 제목을 입력하세요:",
        key="blog_title_widget",
        placeholder="ex) 삼성전자 갤럭시 Z 플립4 사용후기"
    )

    if st.button("AI 추천 제목"):
        # GPT로부터 제목 생성 -> 모달 오픈
        regenerate_titles_cb()
        ai_titles_modal.open()


    product_specs_list = st_tags(
        label='제품 스펙',
        text='스펙 입력 후 엔터/스페이스',
        value=[],
        suggestions=[],
        maxtags=6,
        key='spec_tags'
    )


    keywords_list = st_tags(
        label='키워드를 입력하세요(최대10개)',
        text='키워드 입력 후 엔터/스페이스',
        value=[],
        suggestions=[],
        maxtags=10,
        key='keyword_tags'
    )


    # "글 생성" 버튼 -> DB 저장용 최종값
    if st.button("글 생성"):
        final_title = st.session_state["blog_title_widget"]
        if not final_title:
            st.warning("블로그 제목을 입력하거나 AI 추천 제목을 사용해주세요.")
        else:
            result, used_urls = blog_generation_workflow(
                st.session_state["product_name"],
                product_specs_list,
                final_title,
                keywords_list
            )
            if result:
                st.session_state["original_result"] = result
                st.session_state["used_urls"] = used_urls
            else:
                st.warning("글 생성에 실패했습니다.")

# 모달
if ai_titles_modal.is_open():
    with ai_titles_modal.container():
        st.write("AI가 추천한 블로그 제목들을 아래에서 골라주세요.")

        # 라디오: 지역 변수
        selected_title = None
        if st.session_state["suggested_titles"]:
            selected_title = st.radio(
                "제목 선택",
                st.session_state["suggested_titles"],
            )
        else:
            st.write("아직 AI 추천 제목이 없습니다.")

        # 하단 버튼들
        c1, c2, c3 = st.columns([1,1,1])
        with c1:
            st.button("재생성", on_click=regenerate_titles_cb)
        with c2:
            st.button(
                "사용하기",
                on_click=on_use_title_cb,
                args=(selected_title,)
            )
        with c3:
            st.button("닫기", on_click=close_modal_cb)


with right_col:
    with st.container():
        # 글 생성 결과 확인
        if "original_result" not in st.session_state:
            st.markdown(
                "<p style='color: #333; font-size:16px;'>아직 생성된 글이 없습니다. 왼쪽에서 '글 생성' 후 확인해주세요.</p>",
                unsafe_allow_html=True
            )
        else:
            # (1) 본문 렌더링
            import re
            import html

            # 원본 텍스트
            result_text = st.session_state["original_result"]

            # 1) 백틱 제거
            result_text = result_text.replace("```", "")

            # 2) 혹시 &lt;div&gt;처럼 이스케이프되어 있다면 해제
            result_text = html.unescape(result_text)

            # 글자 수 계산
            char_count = len(result_text)
            byte_count = len(result_text.encode("utf-8"))
            no_space_count = len(result_text.replace(" ", "").replace("\n", ""))
            no_space_byte = len(result_text.replace(" ", "").replace("\n", "").encode("utf-8"))

            st.markdown(
                f"""
                <p style="color:#333; font-size:14px;">
                (공백 포함 
                <span style="color:#6c63ff;">{char_count}</span> 자 | 
                <span style="font-weight:600;">{byte_count} byte</span>, 
                공백 제외 
                <span style="color:#6c63ff;">{no_space_count}</span> 자 | 
                <span style="font-weight:600;">{no_space_byte} byte</span> )
                </p>
                """,
                unsafe_allow_html=True
            )

            display_source_html = ""
            source_html = ""

            if "used_urls" in st.session_state and st.session_state["used_urls"]:
                source_html += "<h3 style='font-size:14px;'>스펙 정보 출처</h3>"
                for url in st.session_state["used_urls"]:
                    display_source_html += f"<p> - <a href='{url}' target='_blank'>{url}</a></p>"

            # (2) 둥근 모서리 박스
            st.markdown(
                f"""
                <div style="background-color: #fff;
                            border-radius: 10px;  
                            padding: 20px;
                            margin-top: 20px;
                            border: 1px solid #ddd;
                            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                            color: #333;">
                    {result_text}
                    {source_html}
                    {display_source_html}
                </div>
                """,
                unsafe_allow_html=True
            )

            
            # (3) DB 저장 버튼
            if st.button("제출하기"):
                connection = pymysql.connect(**DB_CONFIG)
                try:
                    with connection.cursor() as cursor:
                        insert_sql = "INSERT INTO blog_posts_1 (title, content) VALUES (%s, %s)"
                        cursor.execute(insert_sql, (blog_title, result_text))
                    connection.commit()
                    st.success("성공적으로 제출되었습니다!")
                except Exception as e:
                    st.error(f"DB 저장 중 오류 발생: {e}")
                finally:
                    connection.close()
