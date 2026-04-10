# Cloud Storage 버킷 생성
resource "google_storage_bucket" "signage" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = false

  website {
    main_page_suffix = "pages/index.html"
    not_found_page   = "pages/index.html"
  }

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}

# 버킷을 공개적으로 읽을 수 있도록 설정
resource "google_storage_bucket_iam_member" "public_reader" {
  bucket = google_storage_bucket.signage.name
  role   = "roles/storage.objectViewer"
  member = "allUsers"
}

# pages 디렉토리의 모든 파일 업로드 (README.md 제외)
resource "google_storage_bucket_object" "pages_files" {
  for_each = { for f in fileset("${path.module}/../pages", "**") : f => f if !endswith(f, "README.md") }

  name   = "pages/${each.value}"
  bucket = google_storage_bucket.signage.name
  source = "../pages/${each.value}"

  content_type = endswith(each.value, ".html") ? "text/html; charset=utf-8" : "application/octet-stream"
  cache_control = endswith(each.value, ".html") ? "public, max-age=300" : "public, max-age=31536000"
}

# public 디렉토리의 모든 파일 업로드
resource "google_storage_bucket_object" "public_files" {
  for_each = fileset("${path.module}/../public", "**")

  name   = "public/${each.value}"
  bucket = google_storage_bucket.signage.name
  source = "../public/${each.value}"

  content_type = endswith(each.value, ".png") ? "image/png" : (endswith(each.value, ".jpg") || endswith(each.value, ".jpeg") ? "image/jpeg" : (endswith(each.value, ".mp4") ? "video/mp4" : "application/octet-stream"))
  cache_control = "public, max-age=31536000"
}
