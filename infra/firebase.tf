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
