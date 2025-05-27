# from agents import Agent, Runner
import openai

from dotenv import load_dotenv
import os
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

openai.api_key = YOUTUBE_API_KEY  # 실제 키로 교체

def call_openai_to_generate_blog(title, content, style):
    style_name_map = {
        "tech": "기술 블로그",
        "daily": "일상 블로그",
        "summary": "요약형 포스트",
        "retrospective": "회고록",
        "tutorial": "튜토리얼/가이드",
        "opinion": "의견/칼럼"
    }
    style_name = style_name_map.get(style, "일반 포스트")

    prompt = f"""
당신은 다양한 스타일의 블로그 글을 작성하는 능력을 가진 블로거입니다.

다음 정보를 바탕으로 {style_name} 스타일의 블로그 포스트를 HTML 형식으로 작성해 주세요.

제목: "{title}"
내용 요약 또는 핵심 아이디어: "{content}"

작성 시 HTML로 구성하되, <h1> 태그로 제목을 표시하고, 글의 스타일을 설명하는 부분을 포함해 주세요.
글 본문은 해당 스타일에 맞게 자유롭게 구성하세요.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "당신은 블로그 콘텐츠를 HTML로 작성하는 전문가입니다."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    return response['choices'][0]['message']['content']
