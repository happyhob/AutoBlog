import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
client = OpenAI(api_key=YOUTUBE_API_KEY)  # 새 방식

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
    목적: 블로그 작성
    블로그 양식: velog 블로그
    주제: {title}

    작성 내용: {content}
    블로그 형식: {style_name_map[style]}

    위의 내용을 토대로 블로그 양식에 맞춰서 이쁘게 내용을 작성해서 반환환
    """


    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 블로그 콘텐츠를 HTML로 작성하는 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    print(response)
    return response.choices[0].message.content
