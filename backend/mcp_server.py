import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)  # 새 방식

def call_openai_to_generate_blog(title, content, style):
    style_name_map = {
        "tech": "기술 블로그",
        "daily": "일상 블로그",
        "summary": "요약형 포스트",
        "retrospective": "회고록",
        "tutorial": "튜토리얼/가이드",
        "opinion": "의견/칼럼"
    }
    # style_name = style_name_map.get(style, "일반 포스트")

    prompt = f"""
        너는 Markdown 형식으로 블로그 글을 쓰는 전문가야.
        작성 목적은 velog 블로그용 글을 작성하는 것이야.

        [블로그 제목]
        {title}

        [글의 주제 및 내용 요약]
        {content}

        [작성 스타일]
        {style_name_map[style]}

        다음 조건을 반드시 지켜줘:
        - Markdown 문법을 꼭 지켜서 작성해줘.
        - 중요한 문장은 **굵게** 처리해줘.
        - 표가 필요한 내용이면 Markdown 표 형식으로 만들어줘.
        - 색상을 넣는 문법은 velog에서는 지원하지 않으니 쓰지 말아줘.
        - 적절한 소제목(##, ### 등)을 활용해서 가독성을 높여줘.
        - 너무 짧지 않게, 구체적이고 풍부하게 써줘.
    """


    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 블로그 콘텐츠를 velog 양식으로 작성하는 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    print(f"response.choices[0].message.content:{response.choices[0].message.content}")
    return response.choices[0].message.content
