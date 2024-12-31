import openai

def get_ai_suggested_titles(product_name, max_suggestions=4):
    """
    GPT에게 블로그 제목을 여러 개 추천해달라고 요청하는 함수 예시
    """
    prompt = f"""
당신은 블로그 제목을 짓는 전문가입니다.
'{product_name}'을 광고하고 사람들이 클릭하고 싶게 만드는 블로그 글 제목을 {max_suggestions}개 추천해줘.
순수하게 제목만 남겨줘. 번호와 따옴표도 제거해줘.
"""
    response = openai.ChatCompletion.create(
        model="o1-mini",
        messages=[{"role":"user","content":prompt}]
    )
    ai_text = response.choices[0].message.content.strip()
    titles = ai_text.split("\n")
    return [t.strip("- ").strip() for t in titles if t.strip()]



# prompt = f"""
# 당신은 블로그 제목을 짓는 전문가입니다.
# '{product_name}'을 광고하는 블로그 글 제목을 {max_suggestions}개 추천해줘.
# 순수하게 제목만 남겨줘. 번호와 따옴표도 제거해줘.
# """