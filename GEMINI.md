# 업무 말투 변환기 (Business Tone Converter) - 프로젝트 컨텍스트

이 파일은 프로젝트의 개요, 기술 스택, 개발 규칙 및 실행 방법을 정의합니다. Gemini CLI와 같은 AI 에이전트가 프로젝트를 이해하고 일관성 있게 작업을 수행하는 데 도움을 줍니다.

---

## 1. 프로젝트 개요
**업무 말투 변환기**는 사용자가 입력한 메시지를 수신 대상(상사, 동료, 고객 등)에 적합한 비즈니스 말투로 변환해주는 서비스입니다. 

- **목표**: 직장 내 커뮤니케이션 비용 감소 및 정중한 비즈니스 언어 사용 지원.
- **주요 기능**: 
    - 텍스트 입력 및 수신 대상 선택(상사, 타팀 동료, 고객, 팀 내 동료).
    - Upstage Solar-Pro2 AI 모델을 활용한 말투 변환.
    - 변환 결과 출력 및 복사 기능.

## 2. 기술 스택
- **Backend**: Python 3.x, FastAPI
- **Frontend**: HTML, CSS (Vanilla CSS), JavaScript (Vanilla JS)
- **AI Engine**: Upstage Solar-Pro2 API
- **Infrastructure**: Vercel (배포 예정)

## 3. 주요 문서 가이드
- **[PRD_업무말투변환기.md](./PRD_업무말투변환기.md)**: 제품 요구사항 명세서. 기능 요구사항, API 명세, 단계별 구현 가이드 포함.
- **[개요서_업무말투변환기.md](./개요서_업무말투변환기.md)**: 프로그램의 목적과 기대 효과 설명.
- **[my-rules.md](./my-rules.md)**: AI 에이전트를 위한 작업 원칙 및 금지 사항.

## 4. 개발 및 실행 환경 (예정)

### 백엔드 (FastAPI)
- **실행 명령어**: `uvicorn main:app --reload`
- **의존성 설치**: `pip install fastapi uvicorn requests python-dotenv` (추후 `requirements.txt` 생성 예정)
- **환경 변수**: `.env` 파일에 `SOLAR_API_KEY` 설정 필요.

### 프론트엔드
- `index.html`을 브라우저에서 직접 열거나 로컬 서버로 실행.

## 5. 프로젝트 작업 원칙 (from my-rules.md)
1. **언어**: 모든 응답 및 주석은 **한국어**를 기본으로 합니다.
2. **보안**: `.env` 파일의 API 키 등 민감 정보는 절대 출력하거나 외부에 노출하지 않습니다.
3. **신중한 작업**: `git reset --hard`, `git push --force` 등 파괴적인 작업은 금지됩니다.
4. **선 조사 후 구현**: 새로운 기술이나 API 적용 전에는 먼저 조사하고 계획을 공유합니다.
5. **에러 분석 우선**: 버그 발생 시 즉시 수정하기보다 원인을 먼저 분석하여 보고합니다.

## 6. 디렉토리 구조 (계획)
```text
.
├── main.py              # FastAPI 백엔드 메인 로직
├── api/                 # API 엔드포인트 및 비즈니스 로직
├── static/              # 프론트엔드 정적 파일 (index.html, style.css, script.js)
├── .env                 # 환경 변수 (API KEY 등) - GIT 무시 대상
├── .gitignore           # Git 제외 설정
├── PRD_업무말투변환기.md  # 요구사항 명세서
├── 개요서_업무말투변환기.md # 프로그램 개요서
└── GEMINI.md            # 프로젝트 컨텍스트 (본 파일)
```

### Git Commit 와 Push를 반드시 확인을 받고 수행하세요. 임의로 Remote Repository에 Push 하면 절대로 안됨.


---
*마지막 업데이트: 2026-04-22*
