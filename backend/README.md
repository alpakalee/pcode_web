# 백엔드 (Backend)

이 디렉토리는 P-CODE 웹사이트의 백엔드 서버 코드를 포함하고 있습니다.

## 기술 스택

- **언어**: Python 3.9+
- **프레임워크**: Flask
- **데이터베이스**: PostgreSQL
- **API**: RESTful API
- **인증**: 세션 기반 인증

## 구조

```
backend/
├── app.py                # 메인 애플리케이션 파일
├── requirements.txt      # 의존성 패키지 목록
├── models/               # 데이터베이스 모델
├── routes/               # API 라우트
├── services/             # 비즈니스 로직
├── utils/                # 유틸리티 함수
└── tests/                # 테스트 코드
```

## 환경 설정

### 1. 필요 조건

- Python 3.9 이상
- PostgreSQL 13 이상
- pip (Python 패키지 관리자)

### 2. 환경 변수 설정

백엔드 서버는 다음 환경 변수를 사용합니다. `.env` 파일을 생성하여 설정하세요:

```
DB_HOST=localhost
DB_NAME=pcode_db
DB_USER=postgres
DB_PASSWORD=your_password
SECRET_KEY=your_secret_key
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 서버 실행

```bash
python app.py
```

서버는 기본적으로 `http://localhost:5000`에서 실행됩니다.

## API 문서

### 인증 API

| 엔드포인트 | 메소드 | 설명 |
|------------|--------|------|
| `/api/register` | POST | 새 사용자 등록 |
| `/api/login` | POST | 사용자 로그인 |
| `/api/logout` | POST | 로그아웃 |
| `/api/user` | GET | 현재 사용자 정보 조회 |

### 비즈니스 로직 API (예정)

| 엔드포인트 | 메소드 | 설명 |
|------------|--------|------|
| `/api/ctf/challenges` | GET | CTF 문제 목록 조회 |
| `/api/ctf/challenge/:id` | GET | 특정 CTF 문제 조회 |
| `/api/board/posts` | GET | 게시글 목록 조회 |
| `/api/board/post/:id` | GET | 특정 게시글 조회 |

## 개발 가이드라인

### 코드 스타일

- PEP 8 스타일 가이드를 따릅니다
- 함수, 클래스, 모듈에 적절한 문서화(docstring)를 추가하세요
- 변수명, 함수명은 가독성 있게 작성하세요

### 기여 방법

1. 개발 전 이슈를 생성하세요
2. 기능 개발은 새 브랜치에서 진행하세요: `feature/기능명`
3. 버그 수정은 새 브랜치에서 진행하세요: `fix/버그명`
4. 변경사항은 테스트와 함께 제출하세요
5. Pull Request를 생성하고 코드 리뷰를 요청하세요

## 테스트

### 테스트 실행

```bash
python -m pytest tests/
```

## 트러블슈팅

- 데이터베이스 연결 문제: 환경 변수 설정을 확인하세요
- 인증 관련 문제: 세션 구성과 secret_key 설정을 확인하세요
- API 호출 실패: 로그 확인 및 엔드포인트 URL 검증을 진행하세요 