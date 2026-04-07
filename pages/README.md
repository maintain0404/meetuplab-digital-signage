# Pages 디렉토리

`pages/index.html`은 각 디지털 사이니지 화면을 미리보기하고 설정을 관리할 수 있는 대시보드입니다.

## 개요

### 기능
- 여러 화면을 한눈에 미리보기
- 각 화면의 설정을 쿼리 파라미터로 조정
- "미리보기" 버튼: 작은 화면에서 설정 확인
- "전체화면으로" 버튼: 선택한 설정으로 전체화면 재생

## 쿼리 파라미터 시스템

### 작동 원리

이 시스템은 **input/select 요소의 `name` 어트리뷰트를 쿼리 파라미터로 자동 변환**합니다.

```
input/select의 name="파라미터명" value="값"
       ↓
URL: ./rotating-logos/index.html?파라미터명=값
```

### 현재 사용 가능한 파라미터

#### Rotating Logos
| 파라미터 | 가능한 값 | 설명 |
|---------|---------|------|
| `rotating-theme` | `light`, `dark`, (빈 값) | 표시 모드 (비어있으면 시스템 기본값) |

**예시 URL:**
```
./rotating-logos/index.html?rotating-theme=dark
```

#### Logo with Video
| 파라미터 | 가능한 값 | 설명 |
|---------|---------|------|
| `video-id` | YouTube 동영상 ID | 재생할 유튜브 동영상 |
| `video-theme` | `light`, `dark`, (빈 값) | 표시 모드 (비어있으면 시스템 기본값) |

**예시 URL:**
```
./logo-with-video/index.html?video-id=abc123&video-theme=dark
```

## 새로운 섹션 추가하기

### 1단계: HTML 마크업 추가

`pages/index.html`에 새로운 섹션을 추가합니다. 기존 섹션 구조를 참고하세요. 

```html
<div class="small-page-container">
    <h3>섹션 제목</h3>
    
    <div class="small-page-wrapper">
        <iframe 
            id="new-iframe"
            src="./new-page/index.html" 
            frameborder="0" 
            allow="autoplay; encrypted-media" 
            allowfullscreen
            referrerpolicy="strict-origin-when-cross-origin">
        </iframe>
    </div>
    
    <div class="page-description">
        <p>섹션 설명</p>
    </div>
    
    <div class="page-editor">
        <h4>화면 설정</h4>
        <p class="editor-description">아래 옵션을 선택하여 화면을 커스터마이징할 수 있습니다.</p>
        
        <!-- 여기에 input/select 추가 -->
        <div class="form-group">
            <label for="new-param">
                파라미터 이름
                <span class="form-help">설명</span>
            </label>
            <select id="new-param" name="new-param">
                <option value="">기본값</option>
                <option value="option1">옵션 1</option>
                <option value="option2">옵션 2</option>
            </select>
        </div>
        
        <button onclick="applySettings(this, false)" class="editor-button">미리보기</button>
        <button onclick="applySettings(this, true)" class="editor-button">전체화면으로</button>
    </div>
</div>
```

### 2단계: Name 어트리뷰트 설정 (중요!)

각 input/select 요소에 `name` 어트리뷰트를 설정해야 합니다. 이 값이 **쿼리 파라미터명**이 됩니다. input/select의 `value` 속성으로 기본값을 설정할 수 있습니다:

```html
<!-- ❌ 잘못된 예 -->
<select id="my-option">
    <option value="dark">어두움</option>
</select>

<!-- ✅ 올바른 예 -->
<select id="my-option" name="my-option">
    <option value="dark">어두움</option>
</select>
```

### 3단계: 파라미터 목록 문서화

이 README의 "사용 가능한 파라미터" 섹션에 새로운 파라미터를 추가합니다.

```markdown
#### New Section
| 파라미터 | 가능한 값 | 설명 |
|---------|---------|------|
| `new-param` | `option1`, `option2` | 파라미터 설명 |
```

## JavaScript 자동화

`applySettings` 함수는 다음을 자동으로 처리합니다:

1. **부모 컨테이너 파악**: 클릭한 버튼의 `small-page-container`를 찾음
2. **모든 입력값 수집**: 해당 컨테이너의 모든 `name` 어트리뷰트를 가진 요소 검색
3. **URL 생성**: name과 value를 쿼리 파라미터로 변환
4. **iframe 업데이트**: 생성된 URL로 iframe src 설정
5. **전체화면 전환** (선택시): 요청하면 전체화면 모드로 재생

즉, **새로운 input/select만 추가하면 JavaScript 수정 없이 자동으로 작동합니다!**

## 팁

### URL 직접 입력
쿼리 파라미터를 직접 입력하여 특정 설정으로 바로 접속할 수 있습니다:

```
http://localhost:8000/pages/index.html?rotating-theme=dark&video-id=xyz789&video-theme=light
```
