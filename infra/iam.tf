# Firebase Admin 권한 추가
resource "google_project_iam_member" "firebase_admin" {
  for_each = toset(var.firebase_admin_members)

  project = var.project_id
  role    = "roles/firebase.admin"
  member  = "user:${each.value}"
}

# Editor 역할 (선택사항)
# resource "google_project_iam_member" "editor" {
#   for_each = toset(var.firebase_admin_members)
#
#   project = var.project_id
#   role    = "roles/editor"
#   member  = "user:${each.value}"
# }
