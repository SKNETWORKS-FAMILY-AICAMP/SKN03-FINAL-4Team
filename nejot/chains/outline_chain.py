import openai
from nejot.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def create_outline_with_additional_info(product_name, specs_info_list, blog_title, keywords):
    combined_info = ""
    for spec, db_info, web_info in specs_info_list:
        combined_info += f"스펙: {spec}\nDB정보:\n{db_info}\n웹 검색 정보:\n{web_info}\n\n"

    prompt = f"""
    다음은 제품명이야.
    제품명: {product_name}
    다음은 스펙들에 대한 상세정보야.
    {combined_info}

    키워드: {keywords}
    블로그 제목: {blog_title}

    위 정보들을 반영해서 블로그 글의 목차(아웃라인)를 만들어줘.
    각 목차 항목에 간단한 설명을 추가해줘.
    간단한 설명은 스펙에 대한 상세정보를 참고해서 독자가 보기에 객관적이고 구체적이고 수치화된 스펙을 확인할 수 있게 끔 작성해줘.
    목차 항목을 풍부하게 구성해줘.
    본론은 적당하게 최대 4개까지만 만들어줘.
    그리고 블로그 seo 요소를 반영해줘.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"너는 프로페셔널 광고성 블로그 글 기획자다."},
            {"role":"user","content": prompt}
        ],
        
        max_tokens=3000
    )
    outline = response.choices[0].message.content
    return outline, combined_info
