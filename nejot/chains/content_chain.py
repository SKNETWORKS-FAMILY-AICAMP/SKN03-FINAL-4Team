from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

def generate_blog_content(outline, blog_title, keywords, product_name, openai_api_key):
    content_prompt = PromptTemplate(
        input_variables=["outline"],
        template=f"""
        목차:
        {{outline}}

        블로그 제목: {blog_title}
        키워드: {keywords}
        제품명: {product_name}

        여기까지 블로그 글 작성을 위한 가이드라인 및 참고할 정보야.

        이 정보를 기반으로 풍부한 설명과 사람이 작성한 것 같은 담백한 광고성 블로그 글(seo요소 포함)을 작성해주세요.
        그리고 애니메이션 캐릭터같이 귀여운 말투로 작성해주세요.
        최대한 전문적이고 설득력 있게 작성해주세요.
        그리고 번호와 본론 서론같은 단어는 제거하되 마크다운 형식은 유지해줘. 인위적이지 않고 자연스럽게 작성해줘.
        """
    )

    llm_gpt = ChatOpenAI(
        openai_api_key=openai_api_key,
        model_name="o1-mini",
        temperature=1
    )

    content_chain = LLMChain(llm=llm_gpt, prompt=content_prompt)
    generated_content = content_chain.run({"outline": outline})
    return generated_content




# template=f"""
#         다음은 블로그 글 작성 가이드라인이다.

#         목차:
#         {{outline}}

#         블로그 제목: {blog_title}
#         키워드: {keywords}
#         제품명: {product_name}

#         목차를 읽고 목차를 그대로 복사하지 말고, 목차를 기반으로 목차의 각 항목에 대한 풍부한 설명을 포함한 새로운 광고성 블로그 글을 작성해주세요.
#         그리고 애니메이션 캐릭터같이 귀여운 말투로 작성해주세요.
#         최대한 전문적이고 설득력 있게 작성해줘.
#         """