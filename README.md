# 보안 동아리 웹사이트

보안 동아리의 CTF 문제 공유 및 지식 공유 플랫폼입니다.

## 프로젝트 개요

이 프로젝트는 보안 동아리 회원들이 CTF 문제를 공유하고, 보안 지식을 공유할 수 있는 웹 플랫폼을 제공합니다. 주요 기능으로는 CTF 문제 업로드 및 관리, 플래그 제출 및 검증 시스템, 보안 게시판 등이 있습니다.

## 주요 기능

- **CTF 문제 환경**: 다양한 유형의 보안 문제(웹, 시스템 해킹, 암호학, 디지털 포렌식 등) 호스팅
- **지식 공유 플랫폼**: 노션 스타일의 마크다운 지원 게시판으로 보안 지식 공유
- **사용자 관리**: 개인 및 팀 기반 계정 시스템, 점수 보드 등

## 기술 스택

- **서버 환경**: Linux (Ubuntu Server)
- **백엔드**: Flask (Python)
- **프론트엔드**: HTML, CSS, JavaScript (향후 React 또는 Vue.js 도입 예정)
- **데이터베이스**: PostgreSQL
- **컨테이너화**: Docker, Docker Compose

## 저장소 구조

```
pcode_web/
├── docker/                   # 도커 컨테이너 구성 파일
├── backend/                  # 백엔드 코드
├── frontend/                 # 프론트엔드 코드
├── challenges/               # CTF 문제 저장소
│   ├── web/                  # 웹 해킹 관련 문제
│   ├── pwn/                  # 시스템 해킹 관련 문제
│   ├── crypto/               # 암호학 관련 문제
│   └── forensics/            # 디지털 포렌식 관련 문제
├── docs/                     # 문서화 및 가이드라인
├── scripts/                  # 배포 및 유틸리티 스크립트
├── .github/                  # GitHub CI/CD 및 워크플로우
│   └── workflows/            # GitHub Actions 워크플로우
├── .env.example              # 환경 변수 예제 파일
├── docker-compose.yml        # 도커 컴포즈 설정
├── CONTRIBUTING.md           # 기여 가이드라인
└── README.md                 # 프로젝트 설명
```

## 환경 설정 및 보안 안내

### 환경 변수 설정
1. `docker-compose.env.example` 파일을 복사하여 `docker-compose.env` 파일을 생성합니다.
```bash
cp docker-compose.env.example docker-compose.env
```

2. `docker-compose.env` 파일의 민감한 정보를 수정합니다:
   - `<your_secure_password>`: 강력한 비밀번호로 변경 (특수문자, 숫자, 대소문자 포함 12자 이상 권장)
   - `<your_random_secret_key>`: 랜덤한 문자열 생성 (32자 이상 권장)
   - `<your_domain>`: 사용할 도메인 이름으로 변경
   - 데이터베이스 접속 정보 및 기타 민감한 설정 수정

3. 프로덕션 환경 설정:
   - `FLASK_ENV=production` 설정 확인
   - `FLASK_DEBUG=0` 설정 확인 (프로덕션에서는 디버그 모드 비활성화)

### 보안 주의사항
- `.env` 파일이나 `docker-compose.env` 파일은 절대 Git에 커밋하지 마세요.
- `.gitignore` 파일에 민감한 환경 파일이 제외되었는지 확인하세요.
- 주기적으로 모든 비밀번호와 키를 변경하세요.
- 프로덕션 환경에서는 개발 모드를 비활성화하세요.

## 시작하기
```bash
# 환경 설정 준비
cp docker-compose.env.example docker-compose.env
# 환경 변수 편집
nano docker-compose.env

# Docker 컨테이너 실행
docker-compose up -d
```

## 설치 및 실행 방법

### 필요 조건

- Docker 및 Docker Compose
- Git

### 설치 단계

1. 저장소 클론:
   ```bash
   git clone https://github.com/your-username/pcode_web.git
   cd pcode_web
   ```

2. 환경 변수 설정:
   ```bash
   cp docker-compose.env.example docker-compose.env
   # 환경 변수 값을 적절히 수정하세요
   ```

3. Docker 컨테이너 실행:
   ```bash
   docker-compose up -d
   ```

4. 서비스 접속:
   - 웹사이트: http://localhost 또는 http://pcode.ddns.net
   - CTF 플랫폼: http://localhost/ctf 또는 http://pcode.ddns.net/ctf
   - 백엔드 API: http://localhost/api 또는 http://pcode.ddns.net/api

### 개발 환경 실행

개발 모드로 실행하려면:

```bash
# 백엔드 개발
cd backend
pip install -r requirements.txt
python app.py

# 프론트엔드 개발 (정적 파일)
# 프론트엔드 파일을 수정하고 브라우저에서 확인하세요
```

## 폴더별 문서

각 주요 폴더에는 해당 부분에 대한 자세한 문서가 포함되어 있습니다:

- [백엔드 문서](backend/README.md)
- [프론트엔드 문서](frontend/README.md)
- [Docker 환경 문서](docker/README.md)
- [CTF 문제 가이드](challenges/README.md)

## 문제 해결

- **도커 관련 문제**: 컨테이너 로그 확인: `docker-compose logs`
- **백엔드 API 문제**: 백엔드 로그 확인: `docker-compose logs backend`
- **데이터베이스 문제**: 데이터베이스 로그 확인: `docker-compose logs db`

## 라이센스

MIT 라이센스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요. 
