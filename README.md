# 블로그 스타일 게시글 작성 애플리케이션

이 애플리케이션은 FastAPI를 이용한 Python 백엔드와 HTML/CSS/JavaScript를 이용한 프론트엔드로 구성된 간단한 블로그 스타일 게시글 작성 도구입니다.

📦 프로젝트 구조

`
project/
├── backend/
│   ├── main.py
│   └── ...
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
`

##🖥️ 백엔드 (FastAPI)

🔧 환경 설정
1. 가상환경 생성:

`bash
python -m venv env
`

2.가상환경 활성화 (Windows 기준):

`bash
cd env/Scripts
activate
`

3.필수 패키지 설치:
`bash
pip install uvicorn pydantic fastapi
`

▶️ 서버 실행
`bash
uvicorn main:app --reload
`



## 🌐 프론트엔드 (HTML / CSS / JavaScript)
✍️ 기능 설명
제목 입력 필드: 사용자가 게시글 제목을 입력할 수 있습니다.

내용 입력창: 게시글의 본문을 작성할 수 있는 텍스트 영역.

스타일 선택: 블로그 스타일을 선택할 수 있는 옵션을 제공.

전송 버튼: 입력한 데이터를 백엔드로 전송.


## 🔁 동작 흐름
사용자가 제목, 내용을 입력하고 스타일을 선택합니다.

프론트엔드에서 해당 정보를 JSON 형태로 FastAPI 백엔드에 전송합니다.

FastAPI는 해당 데이터를 수신하여 처리하거나 저장합니다.

# 서버 실행 후
`bash
http://localhost:8000 에서 프론트엔드 실행
`

## 📌 참고
FastAPI 공식 문서: https://fastapi.tiangolo.com/

HTML/CSS/JS 기본 참고 문서: [MDN Web Docs
](https://developer.mozilla.org/ko/)
