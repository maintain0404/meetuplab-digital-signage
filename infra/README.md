# OpenTofu 배포 가이드

## 📋 사전 준비

### 1. 환경 설정

```bash
# 환경 변수 파일 생성
cp .env.example .env

# .env 파일 편집 (실제 값 입력)
# - project_id: GCP 프로젝트 ID
# - bucket_name: Cloud Storage 버킷명
# - region: GCP 리전 (기본값: asia-northeast3)
nano .env

# 환경 변수 로드
source .env
```

### 2. GCP 인증

```bash
# Google Cloud CLI 설치 및 로그인
gcloud auth application-default login

# 또는 서비스 계정 키 사용
export GOOGLE_CREDENTIALS="/path/to/service-account-key.json"
```

## 🚀 배포 프로세스

### 초기 설정
```bash
# 1. OpenTofu 초기화
tofu init

# 2. 배포 계획 미리 확인
tofu plan -out=tfplan

# 3. 계획 검토 후 배포
tofu apply tfplan
```

### 기존 배포 업데이트
```bash
# 1. 상태 확인
tofu state list

# 2. 변경사항 확인
tofu plan

# 3. 적용
tofu apply -auto-approve
```

## 🔐 환경 변수 관리

### 환경 변수 우선순위 (높음 → 낮음)
1. 명령행 옵션: `-var "project_id=xxx"`
2. 환경 변수: `export TF_VAR_project_id="xxx"`
3. terraform.tfvars 파일
4. terraform.tfvars.json 파일
5. variables.tf 기본값

### 환경별 설정
```bash
# 개발 환경
cp .env.example .env.dev
# 편집 후
source .env.dev
tofu plan -out=tfplan.dev

# 스테이징 환경
cp .env.example .env.staging
source .env.staging
tofu plan -out=tfplan.staging
```

## 🗂️ 파일 설명

| 파일 | 설명 |
|------|------|
| `provider.tf` | GCP 프로바이더 설정 |
| `variables.tf` | 입력 변수 정의 |
| `main.tf` | 리소스 정의 (Cloud Storage, IAM 등) |
| `outputs.tf` | 배포 후 출력값 |
| `.env.example` | 환경 변수 템플릿 |
| `terraform.tfvars.example` | Terraform 변수 템플릿 |

## 📊 상태 관리

```bash
# 현재 상태 확인
tofu state list

# 특정 리소스 상태 조회
tofu state show 'google_storage_bucket.signage'

# 상태 마이그레이션 (수동)
tofu state mv old_name new_name
```

## 🐛 문제 해결

### 캐시 문제
```bash
# 전체 재초기화
rm -rf .terraform
rm .terraform.lock.hcl  # ⚠️ 먼저 버전 관리에 커밋하세요
tofu init
```

### 상태 불일치
```bash
# 상태 새로고침
tofu refresh

# 또는 원격 상태 강제 동기화
tofu apply -refresh-only
```

## ✅ 배포 후 확인

```bash
# 출력값 확인
tofu output

# GCP 콘솔에서 확인
# https://console.cloud.google.com/storage/browser/meetuplab-signage
```

## 📝 주의사항

- ⚠️ `terraform.tfvars`는 절대 버전 관리에 포함하지 마세요
- ✅ `.terraform.lock.hcl`은 반드시 버전 관리에 포함하세요
- 🔒 서비스 계정 키는 안전한 위치에 보관하세요
- 📊 상태 파일은 자동 백업됩니다 (`*.backup`)
