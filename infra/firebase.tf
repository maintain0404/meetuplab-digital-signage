# GCP 프로젝트에 Firebase 활성화
resource "google_firebase_project" "default" {
  provider = google-beta
  project  = var.project_id
}

# Firebase Hosting 사이트 생성
resource "google_firebase_hosting_site" "default" {
  provider = google-beta
  project  = var.project_id
  site_id  = var.project_id

  depends_on = [google_firebase_project.default]
}

# GitHub Actions용 서비스 계정
resource "google_service_account" "github_actions" {
  project      = var.project_id
  account_id   = "github-actions-firebase"
  display_name = "GitHub Actions Firebase"
}

resource "google_project_iam_member" "github_actions_firebase_admin" {
  project = var.project_id
  role    = "roles/firebase.admin"
  member  = "serviceAccount:${google_service_account.github_actions.email}"
}

# 서비스 계정 키 생성
resource "google_service_account_key" "github_actions" {
  service_account_id = google_service_account.github_actions.name
}
