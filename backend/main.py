from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mcp_server import call_openai_to_generate_blog

app = FastAPI()

# CORS 설정: 프론트엔드(localhost 등)에서 호출 가능하도록 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발 중에는 *로 두고, 배포 시에는 특정 도메인으로 제한하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 요청 형식을 위한 Pydantic 모델 정의
class PostRequest(BaseModel):
    postTitle: str
    postContent: str
    blogStyle: str

@app.post("/generate-post")
async def generate_post(data: PostRequest):
    title = data.postTitle
    content = data.postContent
    style = data.blogStyle

    response =call_openai_to_generate_blog(title,content,style)
    print(response)

    
    # 스타일에 따라 포스트 내용 구성
    style_name_map = {
        "tech": "기술 블로그",
        "daily": "일상 블로그",
        "summary": "요약형 포스트",
        "retrospective": "회고록",
        "tutorial": "튜토리얼/가이드",
        "opinion": "의견/칼럼"
    }
    style_name = style_name_map.get(style, "일반 포스트")

    html = f"""
    <h1>{title}</h1>
    <p class="text-gray-500 italic">스타일: {style_name}</p>
    <div class="border-l-4 border-blue-500 pl-4 my-4 italic text-gray-600">"{content}"</div>
    """

    if style == "tech":
        html += """
        <h2>기술적 배경</h2>
        <p>이 기술은 최근 몇 년간 빠르게 발전해왔으며, 다양한 산업 분야에서 활용되고 있습니다.</p>
        <h2>주요 특징</h2>
        <ul>
            <li>높은 성능과 효율성</li>
            <li>간편한 통합 가능성</li>
            <li>강력한 커뮤니티 지원</li>
        </ul>
        <h2>결론</h2>
        <p>이 기술은 앞으로도 발전 가능성이 크며, 주의 깊게 살펴볼 가치가 있습니다.</p>
        """
    elif style == "daily":
        html += """
        <h2>오늘의 일상</h2>
        <p>하루 동안 있었던 소소한 일들을 돌아보며 기록해봅니다.</p>
        <p>오늘도 평범하지만 감사한 하루였습니다.</p>
        """
    elif style == "summary":
        points = content.split(' ')
        html += f"""
        <h2>핵심 요약</h2>
        <div class="bg-gray-50 p-4 rounded-lg">
            <p>1. { ' '.join(points[:5]) }...</p>
            <p>2. { ' '.join(points[5:10]) }...</p>
            <p>3. { ' '.join(points[10:15]) }...</p>
        </div>
        <h2>참고 사항</h2>
        <p>자세한 내용은 공식 문서나 참고자료를 확인해보세요.</p>
        """
    elif style == "retrospective":
        html += """
        <h2>회고</h2>
        <p>지난 시간 동안의 성장을 돌아보며 얻은 교훈을 정리해봅니다.</p>
        <ul>
            <li>잘한 점: 꾸준히 해낸 나 자신</li>
            <li>개선할 점: 더 나은 시간 관리</li>
        </ul>
        """
    elif style == "tutorial":
        html += """
        <h2>가이드 시작</h2>
        <p>이 튜토리얼은 다음과 같은 단계를 포함합니다:</p>
        <ol>
            <li>준비사항 확인</li>
            <li>핵심 기능 이해</li>
            <li>실습 진행</li>
        </ol>
        """
    elif style == "opinion":
        html += """
        <h2>개인적인 견해</h2>
        <p>이 주제에 대해 다양한 시각이 존재하지만, 제 생각은 이렇습니다...</p>
        """

    return JSONResponse(content={"generatedContent": html})
