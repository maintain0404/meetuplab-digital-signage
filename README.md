# meetuplab-digital-signage
밋업에서 대형 화면에 표시할 디지털 사이니지

## Pages 대시보드
`pages/index.html`에서 각 화면을 미리보기하고 전체화면 할 수 있습니다. 자세한 내용은 [pages/README.md](pages/README.md)를 참고하세요.

## 화면 목록
소스 코드는 src 디렉토리 안에 정의되어 있습니다.
- rotating-logos: 정중앙에 크게 로고가 있고, 배경으로 작은 로고 여러개가 제자리에서 전부 다른 무작위 속도로 회전하는 화면, [디렉토리 링크](src/rotating-logos)
- logo-with-video: 정중앙에 크게 로고가 있고, 배경으로 비디오가 있는 화면, [디렉토리 링크](src/logo-with-video)
- scrolling-logo: 여러 열의 로고가 각기 다른 속도로 수평 이동하는 배경 위에, 잊을 수 없는 대형 히어로 로고가 부유하는 화면, [디렉토리 링크](pages/scrolling-logo)

## 개발자 & LLM용 개발 가이드

### 핵심 원칙

1. 반드시 **public/images 하에 로고 파일**을 적극적으로 활용하고 로고가 굉장히 슈퍼 잘 돋보이는 화면을 구현해야 합니다.
2. 텍스트는 로고에 적힌 문구만 활용해주세요.
3. 다크모드 라이트모드를 둘 다 만들어주세요
4. 아무런 외부 인터렉션 없이도 화면에 움직임이 있어야 합니다.
5. 이 파일의 화면 목록에도 추가해주세요

### 새로운 섹션 추가

1. **pages/\~~\~~/index.html , pages/\~~\~~/README.md 추가
   - 디렉토리 이름은 영문 소문자, 숫자와 -만 사용 가능
   - 쿼리 파라미터를 옵션으로 사용. 쿼리파라미터 이름은 camelCase로 작명

2. **pages/index.html에 마크업 추가** (섹션 구조는 pages/README.md에 있는 기존 섹션 참고)
   - `<div class="small-page-container">` 추가
   - `name` 어트리뷰트를 가진 input/select 작성. name은 1에서 정한 쿼리파라미터 이름과 같음
   - iframe의 id는 1에서 정한 디렉토리명과 같음

3. **pages/README.md에 파라미터 문서화**
   - 해당 섹션에 파라미터 테이블 추가

**주의:** `applySettings` 함수 수정은 불필요합니다.

더 자세한 내용은 [pages/README.md](pages/README.md)를 참고하세요.

### 테스트
pytest를 사용합니다. `mise run test`로 실행합니다.

### 포매팅
ruff를 사용합니다. `mise run format`로 실행합니다.

