# Tests for Development Guidelines

이 디렉토리는 [README.md](../README.md)의 "개발자 & LLM용 개발 가이드"에 정의된 규칙들을 pytest로 검증합니다.

## 테스트 항목

### TestPageNameConvention
- ✅ 페이지 디렉토리명은 영문 소문자, 숫자, -만 사용

### TestIframeStructure
- ✅ 각 섹션의 iframe은 id 어트리뷰트가 있음
- ✅ 각 페이지 디렉토리에 index.html이 있음

### TestQueryParameterNaming
- ✅ Input/select의 name 어트리뷰트는 camelCase

### TestPageDocumentation
- ✅ pages/README.md가 존재
- ✅ 주요 섹션이 문서화됨

### TestConsistency
- ✅ 각 섹션에 미리보기/전체화면 버튼이 있음
- ✅ 버튼이 applySettings를 호출
- ✅ 각 섹션에 설정용 입력 요소가 있음

## 실행 방법

### 1. 의존성 설치 (uv 사용)

```bash
# Python 환경 설정 (Python 3.8+)
uv venv

# 의존성 설치
uv pip install -e ".[dev]"

# 또는 직접 설치
uv pip install pytest>=7.0 beautifulsoup4>=4.11
```

### 2. mise를 사용하는 경우

```bash
# .mise.toml에 정의된 작업 실행
mise run test
```

### 3. 테스트 실행

```bash
# 모든 테스트 실행
python -m pytest tests/test_conventions.py -v

# 특정 테스트 클래스만 실행
python -m pytest tests/test_conventions.py::TestPageNameConvention -v

# 상세 출력과 함께 실행
python -m pytest tests/test_conventions.py -vv
```

## 테스트 결과 해석

- ✓ 통과: 규칙을 따르고 있음
- ✗ 실패: 규칙을 위반함 (수정 필요)
- ⚠ 경고: 현재 코드 상태 정보 (수정 권장)

## 예시

새로운 섹션을 추가할 때:

```html
<!-- pages/index.html -->
<div class="small-page-container">
    <h3>New Section</h3>
    <div class="small-page-wrapper">
        <iframe id="new-section" src="./new-section/index.html"></iframe>
    </div>
    <div class="page-editor">
        <input type="text" name="myParameter" value="">
        <button onclick="applySettings(this, false)">미리보기</button>
        <button onclick="applySettings(this, true)">전체화면으로</button>
    </div>
</div>
```

위 마크업이 검증되는 항목들:
1. ✓ 디렉토리명 `new-section` (영문 소문자, -)
2. ✓ iframe id `new-section` (디렉토리명과 일치)
3. ✓ input name `myParameter` (camelCase)
4. ✓ 버튼이 `applySettings` 호출
