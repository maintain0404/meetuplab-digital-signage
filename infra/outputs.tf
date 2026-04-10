output "bucket_name" {
  description = "Cloud Storage bucket name"
  value       = google_storage_bucket.signage.name
}

output "bucket_url" {
  description = "Cloud Storage bucket public URL"
  value       = "https://storage.googleapis.com/${google_storage_bucket.signage.name}"
}

output "website_url" {
  description = "Website URL"
  value       = "https://${google_storage_bucket.signage.name}.storage.googleapis.com"
}

output "firebase_hosting_url" {
  description = "Firebase Hosting URL"
  value       = "https://${google_firebase_hosting_site.default.site_id}.web.app"
}
