# CTF 문제 저장소

이 디렉토리는 P-CODE 웹사이트의 CTF(Capture The Flag) 문제를 포함하고 있습니다.

## 문제 카테고리

CTF 문제는 다음 카테고리로 구성됩니다:

- **web**: 웹 해킹 관련 문제
- **pwn**: 시스템 해킹, 바이너리 취약점 관련 문제
- **crypto**: 암호학 관련 문제
- **forensics**: 디지털 포렌식 관련 문제
- **misc**: 기타 문제 (스테가노그래피, OSINT 등)
- **reverse**: 리버스 엔지니어링 관련 문제

## 문제 디렉토리 구조

각 문제는 다음과 같은 구조로 구성됩니다:

```
challenges/
├── 카테고리/
│   └── 문제명/
│       ├── Dockerfile              # 문제 환경 구성
│       ├── docker-compose.yml      # 복잡한 환경의 경우
│       ├── src/                    # 소스 코드
│       ├── dist/                   # 참가자에게 제공할 파일
│       ├── solution/               # 출제자 솔루션
│       │   ├── solution.py         # 솔루션 스크립트
│       │   └── writeup.md          # 솔루션 설명
│       ├── challenge.json          # 문제 메타데이터
│       └── README.md               # 문제 설명
```

## 문제 등록 방법

### 1. 디렉토리 생성

문제의 카테고리와 이름으로 디렉토리를 생성합니다:

```bash
mkdir -p challenges/web/simple-xss
```

### 2. challenge.json 작성

문제의 메타데이터를 포함하는 `challenge.json` 파일을 작성합니다:

```json
{
  "name": "Simple XSS",
  "category": "web",
  "description": "**문제 설명**\n\n간단한 XSS 취약점을 발견하고 관리자의 쿠키를 탈취하세요.\n\n**접속 정보**\nhttp://simple-xss.pcode.ddns.net",
  "difficulty": "easy",
  "flag": "FLAG{xss_is_still_relevant_in_2023}",
  "points": 100,
  "author": "your_username",
  "tags": ["xss", "web", "javascript"],
  "hints": [
    {"content": "입력 값이 어디에 표시되는지 확인해보세요.", "cost": 10},
    {"content": "alert() 외에 fetch()를 사용해 외부로 데이터를 전송할 수 있습니다.", "cost": 20}
  ]
}
```

### 3. 문제 환경 구성

Docker 환경을 사용하여 문제를 구성합니다. `Dockerfile`을 작성하세요:

```dockerfile
FROM php:7.4-apache

COPY src/ /var/www/html/
RUN chown -R www-data:www-data /var/www/html/

EXPOSE 80
```

### 4. 소스 코드 작성

`src` 디렉토리에 문제에 필요한 소스 코드를 작성합니다.

### 5. 배포 파일 준비

참가자에게 제공할 파일은 `dist` 디렉토리에 저장합니다.

### 6. 솔루션 작성

출제자 솔루션과 풀이 설명을 `solution` 디렉토리에 저장합니다.

## 문제 테스트

### 로컬 환경에서 테스트

```bash
cd challenges/web/simple-xss
docker build -t simple-xss .
docker run -p 8080:80 simple-xss
```

이제 `http://localhost:8080`에서 문제를 테스트할 수 있습니다.

### 솔루션 검증

문제 솔루션이 정상적으로 작동하는지 확인하세요:

```bash
cd challenges/web/simple-xss/solution
python solution.py
```

## 문제 아이디어

다음은 각 카테고리별 문제 아이디어입니다:

### 웹 해킹
- XSS (저장형, 반사형, DOM 기반)
- SQL 인젝션
- 서버 사이드 요청 위조 (SSRF)
- 서버 사이드 템플릿 인젝션 (SSTI)
- 디렉토리 트래버설
- 파일 업로드 취약점

### 시스템 해킹
- 버퍼 오버플로우
- 포맷 스트링 취약점
- 힙 기반 취약점
- Return Oriented Programming (ROP)

### 암호학
- 고전 암호 (시저, 비즈네르, 치환 암호 등)
- RSA 암호 취약점
- 해시 충돌
- 타이밍 공격

### 디지털 포렌식
- 파일 헤더 분석
- 메모리 덤프 분석
- 네트워크 패킷 분석
- 디스크 이미지 분석

## 기여 가이드라인

CTF 문제 제작 시 다음 사항을 고려하세요:

1. **명확한 목표**: 문제가 무엇을 요구하는지 명확하게 설명하세요
2. **적절한 난이도**: 대상 참가자의 수준에 맞는 난이도를 설정하세요
3. **원활한 실행**: Docker 환경이 안정적으로 작동하는지 확인하세요
4. **고유한 플래그**: 플래그 형식은 `FLAG{내용}`을 따르며, 고유하고 추측하기 어렵게 작성하세요
5. **완전한 솔루션**: 출제자 솔루션은 완전하고 재현 가능해야 합니다 