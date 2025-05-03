# 기여 가이드라인

보안 동아리 웹사이트 프로젝트에 기여해 주셔서 감사합니다. 이 문서는 프로젝트에 기여하는 방법에 대한 가이드라인을 제공합니다.

## 기여 방법

### 1. 이슈 확인 및 생성

프로젝트에 기여하기 전에 GitHub 이슈를 확인하세요. 해결하려는 문제가 이미 다른 사람에 의해 작업 중인지 확인할 수 있습니다. 새로운 문제나 기능 요청이 있다면 새 이슈를 생성하세요.

### 2. 저장소 포크 및 클론

1. GitHub에서 저장소를 포크합니다.
2. 포크한 저장소를 로컬에 클론합니다:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pcode_web.git
   cd pcode_web
   ```

### 3. 브랜치 생성

작업을 시작하기 전에 새 브랜치를 생성하세요:
```bash
git checkout -b feature/기능명
# 또는
git checkout -b fix/버그명
```

### 4. 코드 작성 및 테스트

- 코드 스타일 가이드라인을 준수하세요.
- 변경 사항에 대한 테스트를 추가하세요.
- 모든 테스트가 통과하는지 확인하세요.

### 5. 커밋 및 푸시

변경 사항을 커밋하고 푸시하세요:
```bash
git add .
git commit -m "기능: 간결하고 명확한 커밋 메시지"
git push origin feature/기능명
```

커밋 메시지는 다음 형식을 따르세요:
- `기능: 새로운 기능 추가`
- `수정: 버그 수정`
- `문서: 문서 업데이트`
- `테스트: 테스트 추가 또는 수정`
- `리팩터: 코드 리팩토링`

### 6. Pull Request 생성

GitHub에서 원본 저장소에 Pull Request를 생성하세요. PR 설명에는 다음 내용을 포함하세요:
- 변경 사항의 목적
- 관련 이슈 번호 (있는 경우)
- 테스트 방법 (필요한 경우)

## 코드 스타일 가이드라인

### Python 코드
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) 스타일 가이드를 따르세요.
- 들여쓰기는 4칸 공백을 사용하세요.
- 함수, 클래스, 메소드에 적절한 문서 문자열(docstring)을 추가하세요.

### JavaScript 코드
- [Airbnb JavaScript 스타일 가이드](https://github.com/airbnb/javascript)를 따르세요.
- 들여쓰기는 2칸 공백을 사용하세요.
- 세미콜론을 사용하세요.

## 브랜치 관리

- `main`: 안정 버전 브랜치
- `develop`: 개발 브랜치 (주요 통합 지점)
- `feature/*`: 새 기능 개발 브랜치
- `fix/*`: 버그 수정 브랜치
- `docs/*`: 문서 관련 브랜치

## CTF 문제 추가 가이드라인

### 문제 디렉터리 구조

새로운 CTF 문제를 추가할 때는 다음 구조를 따르세요:
```
challenges/카테고리/문제명/
├── Dockerfile                # 문제 환경 구성
├── src/                      # 소스 코드
├── challenge.json            # 메타데이터 (난이도, 카테고리, 힌트 등)
├── solution/                 # 솔루션 및 풀이 설명
└── README.md                 # 문제 설명
```

### challenge.json 형식

```json
{
  "name": "문제 이름",
  "category": "문제 카테고리",
  "description": "문제 설명",
  "difficulty": "쉬움/보통/어려움",
  "flag": "FLAG{이것은_예시_플래그입니다}",
  "points": 100,
  "tags": ["tag1", "tag2"],
  "hints": [
    {"content": "첫 번째 힌트", "cost": 10},
    {"content": "두 번째 힌트", "cost": 20}
  ]
}
```

## 질문 및 도움

질문이나 도움이 필요하면 GitHub 이슈를 통해 문의하세요. 