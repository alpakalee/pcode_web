# Docker 환경 구성

이 디렉토리는 P-CODE 웹사이트의 Docker 컨테이너 구성 파일을 포함하고 있습니다.

## 개요

P-CODE 웹사이트는 다음과 같은 컨테이너로 구성되어 있습니다:

- **nginx**: 웹 서버 및 리버스 프록시
- **backend**: Flask 백엔드 서버
- **db**: PostgreSQL 데이터베이스
- **ctfd**: CTF 문제 관리 시스템

## 디렉토리 구조

```
docker/
├── docker-compose.yml       # 전체 서비스 구성
├── nginx/                   # Nginx 설정
│   ├── Dockerfile           # Nginx 이미지 빌드
│   ├── nginx.conf           # 기본 설정
│   └── sites/               # 사이트별 설정
│       └── default.conf     # 기본 사이트 설정
├── backend/                 # 백엔드 서비스
│   ├── Dockerfile           # Python/Flask 이미지 빌드
│   └── entrypoint.sh        # 컨테이너 실행 스크립트
├── db/                      # 데이터베이스
│   ├── init/                # 초기화 스크립트
│   └── data/                # 데이터 볼륨 (gitignore)
└── ctfd/                    # CTFd 플랫폼
    ├── Dockerfile           # CTFd 이미지 빌드
    └── config.ini           # CTFd 설정 파일
```

## 환경 변수

Docker Compose는 다음 환경 변수를 사용합니다. `.env` 파일을 생성하여 설정하세요:

```
# PostgreSQL 설정
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=pcode_db

# 백엔드 설정
FLASK_ENV=development
DB_HOST=db
DB_NAME=pcode_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
SECRET_KEY=your_very_secret_key

# 도메인 설정
DOMAIN=pcode.ddns.net
```

## 사용 방법

### 서비스 시작

```bash
# 모든 서비스 시작
docker-compose up -d

# 특정 서비스만 시작
docker-compose up -d nginx backend
```

### 서비스 중지

```bash
# 모든 서비스 중지
docker-compose down

# 볼륨 포함하여 모두 제거
docker-compose down -v
```

### 로그 확인

```bash
# 모든 서비스 로그
docker-compose logs

# 특정 서비스 로그
docker-compose logs backend

# 실시간 로그
docker-compose logs -f
```

## Nginx 설정

### SSL 인증서

Let's Encrypt를 통해 SSL 인증서를 발급받아 `docker/nginx/ssl/` 디렉토리에 저장합니다:

- `fullchain.pem`: 인증서 체인
- `privkey.pem`: 개인 키

### 리버스 프록시 설정

Nginx는 다음과 같이 요청을 프록시합니다:

- `/`: 프론트엔드 정적 파일 제공
- `/api/`: 백엔드 서버로 프록시
- `/ctf/`: CTFd 서버로 프록시

## 데이터베이스 관리

### 데이터 백업

```bash
# PostgreSQL 데이터 백업
docker-compose exec db pg_dump -U postgres pcode_db > backup.sql
```

### 데이터 복원

```bash
# PostgreSQL 데이터 복원
cat backup.sql | docker-compose exec -T db psql -U postgres pcode_db
```

## 트러블슈팅

### 컨테이너 접속

```bash
# 백엔드 컨테이너 접속
docker-compose exec backend bash

# 데이터베이스 컨테이너 접속
docker-compose exec db bash
```

### 일반적인 문제

- **네트워크 연결 문제**: 각 서비스의 컨테이너 네트워크 설정 확인
- **권한 문제**: 볼륨 마운트 경로의 권한 확인
- **포트 충돌**: 이미 사용 중인 포트 확인 및 변경

## 개발 팁

- 개발 중에는 볼륨을 마운트하여 소스 코드 변경 사항을 즉시 반영하세요
- Docker의 `restart: always` 옵션을 사용하여 서비스 자동 재시작을 구성하세요
- 프로덕션 환경에서는 로그 로테이션을 구성하세요 