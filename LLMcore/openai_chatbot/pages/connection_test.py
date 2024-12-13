import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import requests


# Page 1
st.title("Connection_test")
st.write("Welcome to Page 1! Use the buttons below to navigate.")

# 버튼으로 페이지 이동
if st.button("Go to Main Page"):
    switch_page("main")

if st.button("Go to Page 2"):
    switch_page("llm_model")

# Streamlit 제목
st.title("FastAPI와 Streamlit 간 송수신 테스트")

# 입력 폼 생성
name = st.text_input("이름 입력:")
value = st.number_input("값 입력:", min_value=0, step=1)

# 버튼 클릭 시 FastAPI로 데이터 송신
if st.button("전송", key="test_butten"):
    url = "https://backdocsend.jamesmoon.click/process/"  # FastAPI 엔드포인트 (fastapi url)
    payload = {"name": name, "value": value}  # 전송할 데이터
    try:
        # FastAPI로 POST 요청
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            # FastAPI 응답 출력
            st.success(f"응답: {response.json()}")
        else:
            st.error(f"에러: {response.status_code} - {response.json()}")
    except requests.exceptions.RequestException as e:
        st.error(f"요청 실패: {e}")


# FastAPI 엔드포인트 URL
BASE_URL = "http://backdocsend.jamesmoon.click/bizcontacts"  # FastAPI의 기본 URL

# Streamlit 타이틀 설정
st.title("BizContacts 정보 조회 및 관리")

# 선택 메뉴
option = st.selectbox("옵션 선택", ["조회: UUID", "조회: Order ID", "데이터 삭제: UUID", "데이터 삭제: Order ID"])

if option == "조회: UUID":
    # UUID로 데이터 조회
    uuid = st.text_input("UUID 입력:")
    if st.button("조회"):
        if uuid:
            try:
                response = requests.get(f"{BASE_URL}/uuid/{uuid}")
                if response.status_code == 200:
                    st.success(f"조회 결과: {response.json()}")
                else:
                    st.error(f"조회 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("UUID를 입력해주세요.")

elif option == "조회: Order ID":
    # Order ID로 데이터 조회
    order_id = st.text_input("Order ID 입력:")
    if st.button("조회"):
        if order_id:
            try:
                response = requests.get(f"{BASE_URL}/order_id/{order_id}")
                if response.status_code == 200:
                    st.success(f"조회 결과: {response.json()}")
                else:
                    st.error(f"조회 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("Order ID를 입력해주세요.")

elif option == "데이터 삭제: UUID":
    # UUID로 데이터 삭제
    uuid = st.text_input("UUID 입력:")
    if st.button("삭제"):
        if uuid:
            try:
                response = requests.delete(f"{BASE_URL}/uuid/{uuid}")
                if response.status_code == 200:
                    st.success("데이터 삭제 성공")
                else:
                    st.error(f"삭제 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("UUID를 입력해주세요.")

elif option == "데이터 삭제: Order ID":
    # Order ID로 데이터 삭제
    order_id = st.text_input("Order ID 입력:")
    if st.button("삭제"):
        if order_id:
            try:
                response = requests.delete(f"{BASE_URL}/order_id/{order_id}")
                if response.status_code == 200:
                    st.success("데이터 삭제 성공")
                else:
                    st.error(f"삭제 실패: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"요청 실패: {e}")
        else:
            st.warning("Order ID를 입력해주세요.")



# st.title("Product Category Viewer")

# # 카테고리 ID 입력
# category_id = st.number_input("카테고리 ID 입력:", min_value=1, step=1, key="category_id_number")

# # 버튼 클릭으로 FastAPI 요청
# if st.button("조회", key="category_id_butten"):
#     url = "http://test-backend-container:8000/productcategories"  # FastAPI URL
#     payload = {"category_id": category_id}  # 요청 데이터

#     try:
#         # FastAPI POST 요청
#         response = requests.post(url, json=payload)

#         if response.status_code == 200:
#             # 응답 데이터를 JSON으로 파싱
#             data = response.json()
#             if "category_name" in data:
#                 st.success(f"카테고리 이름: {data['category_name']}")
#             else:
#                 st.warning("카테고리 이름을 찾을 수 없습니다.")
#         elif response.status_code == 404:
#             st.warning("카테고리를 찾을 수 없습니다.")
#         else:
#             st.error(f"에러 발생: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"요청 실패: {e}")

# st.title("Product Viewer")

# # 입력 필드 생성
# product_id = st.number_input("제품 ID 입력:", min_value=1, step=1, key="product_id_input")

# # 버튼 클릭으로 FastAPI 요청
# if st.button("제품 조회", key="product_id_butten"):
#     # FastAPI 엔드포인트 URL
#     url = "http://test-backend-container:8000/products"
#     payload = {"product_id": product_id}  # 요청 데이터

#     try:
#         # FastAPI에 POST 요청
#         response = requests.post(url, json=payload)

#         # 응답 처리
#         if response.status_code == 200:
#             data = response.json()  # JSON 응답 데이터 파싱
#             if "category_id" in data:
#                 st.success("제품 정보를 성공적으로 가져왔습니다:")
#                 st.write(f"카테고리 ID: {data['category_id']}")
#                 st.write(f"제품명: {data['product_name']}")
#                 st.write(f"브랜드: {data['brand']}")
#                 st.write(f"모델: {data['model']}")
#             else:
#                 st.warning("제품 정보를 찾을 수 없습니다.")
#         elif response.status_code == 404:
#             st.warning("해당 ID의 제품이 없습니다.")
#         else:
#             st.error(f"에러 발생: {response.status_code}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"요청 실패: {e}")
        
        

# # Streamlit 상태 초기화
# if "products_data" not in st.session_state:
#     st.session_state["products_data"] = None

# if "specs_laptop_data" not in st.session_state:
#     st.session_state["specs_laptop_data"] = None

# if "specs_tabletpc_data" not in st.session_state:
#     st.session_state["specs_tabletpc_data"] = None

# if "specs_smartphone_data" not in st.session_state:
#     st.session_state["specs_smartphone_data"] = None

# # 제품 데이터 요청
# product_id = st.number_input("제품 ID 입력:", min_value=1, step=1, key="product_id")
# if st.button("제품 정보 조회"):
#     url = "http://test-backend-container:8000/products"
#     response = requests.post(url, json={"product_id": product_id})
#     if response.status_code == 200:
#         st.session_state["products_data"] = response.json()
#     else:
#         st.error("제품 정보를 가져오지 못했습니다.")

# # 노트북 사양 데이터 요청
# laptop_id = st.number_input("노트북 ID 입력:", min_value=1, step=1, key="laptop_id")
# if st.button("노트북 사양 조회"):
#     url = "http://test-backend-container:8000/specifications_laptop"
#     response = requests.post(url, json={"product_id": laptop_id})
#     if response.status_code == 200:
#         st.session_state["specs_laptop_data"] = response.json()
#     else:
#         st.error("노트북 사양 정보를 가져오지 못했습니다.")

# # 태블릿PC 사양 데이터 요청
# tablet_id = st.number_input("태블릿PC ID 입력:", min_value=1, step=1, key="tablet_id")
# if st.button("태블릿PC 사양 조회"):
#     url = "http://test-backend-container:8000/specifications_tabletpc"
#     response = requests.post(url, json={"product_id": tablet_id})
#     if response.status_code == 200:
#         st.session_state["specs_tabletpc_data"] = response.json()
#     else:
#         st.error("태블릿PC 사양 정보를 가져오지 못했습니다.")

# # 스마트폰 사양 데이터 요청
# smartphone_id = st.number_input("스마트폰 ID 입력:", min_value=1, step=1, key="smartphone_id")
# if st.button("스마트폰 사양 조회"):
#     url = "http://test-backend-container:8000/specifications_smartphone"
#     response = requests.post(url, json={"product_id": smartphone_id})
#     if response.status_code == 200:
#         st.session_state["specs_smartphone_data"] = response.json()
#     else:
#         st.error("스마트폰 사양 정보를 가져오지 못했습니다.")

# # 결과 출력
# if st.session_state["products_data"]:
#     st.write("제품 정보:", st.session_state["products_data"])

# if st.session_state["specs_laptop_data"]:
#     st.write("노트북 사양:", st.session_state["specs_laptop_data"])

# if st.session_state["specs_tabletpc_data"]:
#     st.write("태블릿PC 사양:", st.session_state["specs_tabletpc_data"])

# if st.session_state["specs_smartphone_data"]:
#     st.write("스마트폰 사양:", st.session_state["specs_smartphone_data"])



# st.title("Laptop Specifications Viewer")

# # 제품 ID 입력
# product_laptop_id = st.number_input("제품 ID 입력:", min_value=1, step=1, key='laptop_laptop_id_input')

# # 버튼 클릭으로 FastAPI 요청
# if st.button("사양 조회", key="product_laptop_id_butten"):
#     url = "http://test-backend-container:8000/specifications_laptop"  # FastAPI URL
#     payload = {"product_id": product_id}  # 요청 데이터

#     try:
#         # FastAPI로 POST 요청
#         response = requests.post(url, json=payload)

#         # 응답 처리
#         if response.status_code == 200:
#             data = response.json()  # JSON 응답 데이터 파싱
#             if isinstance(data, list) and len(data) > 0:
#                 st.success(f"제품 ID {product_id}에 대한 사양을 성공적으로 가져왔습니다:")
#                 for spec in data:
#                     st.write(f"- {spec['spec_name']}: {spec['spec_value']}")
#             else:
#                 st.warning(f"제품 ID {product_id}에 대한 사양이 없습니다.")
#         elif response.status_code == 404:
#             st.warning("해당 ID의 제품이 없습니다.")
#         else:
#             st.error(f"에러 발생: {response.status_code} - {response.json().get('detail', 'Unknown Error')}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"요청 실패: {e}")


# st.title("Smartphone Specifications Viewer")

# # 제품 ID 입력
# product_phone_id = st.number_input("제품 ID 입력:", min_value=1, step=1, key="product_phone_id_input")

# # 버튼 클릭으로 FastAPI 요청
# if st.button("사양 조회", key="product_phone_id_butten"):
#     url = "http://test-backend-container:8000/specifications_smartphone"  # FastAPI URL
#     payload = {"product_id": product_id}  # 요청 데이터

#     try:
#         # FastAPI로 POST 요청
#         response = requests.post(url, json=payload)

#         # 응답 처리
#         if response.status_code == 200:
#             data = response.json()  # JSON 응답 데이터 파싱
#             if isinstance(data, list) and len(data) > 0:
#                 st.success(f"제품 ID {product_id}에 대한 사양을 성공적으로 가져왔습니다:")
#                 for spec in data:
#                     st.write(f"- {spec['spec_name']}: {spec['spec_value']}")
#             else:
#                 st.warning(f"제품 ID {product_id}에 대한 사양이 없습니다.")
#         elif response.status_code == 404:
#             st.warning("해당 ID의 제품이 없습니다.")
#         else:
#             st.error(f"에러 발생: {response.status_code} - {response.json().get('detail', 'Unknown Error')}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"요청 실패: {e}")

# st.title("Tabletpc Specifications Viewer")

# # 제품 ID 입력
# product_tabletpc_id = st.number_input("제품 ID 입력:", min_value=1, step=1, key="product_tablet_id_input")

# # 버튼 클릭으로 FastAPI 요청
# if st.button("사양 조회", key="product_tabletpc_id_butten"):
#     url = "http://test-backend-container:8000/specifications_tabletpc"  # FastAPI URL
#     payload = {"product_id": product_id}  # 요청 데이터

#     try:
#         # FastAPI로 POST 요청
#         response = requests.post(url, json=payload)

#         # 응답 처리
#         if response.status_code == 200:
#             data = response.json()  # JSON 응답 데이터 파싱
#             if isinstance(data, list) and len(data) > 0:
#                 st.success(f"제품 ID {product_id}에 대한 사양을 성공적으로 가져왔습니다:")
#                 for spec in data:
#                     st.write(f"- {spec['spec_name']}: {spec['spec_value']}")
#             else:
#                 st.warning(f"제품 ID {product_id}에 대한 사양이 없습니다.")
#         elif response.status_code == 404:
#             st.warning("해당 ID의 제품이 없습니다.")
#         else:
#             st.error(f"에러 발생: {response.status_code} - {response.json().get('detail', 'Unknown Error')}")
#     except requests.exceptions.RequestException as e:
#         st.error(f"요청 실패: {e}")

