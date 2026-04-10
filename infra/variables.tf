variable "project_id" {
  description = "GCP Project ID"
  type        = string
  nullable    = false
}

variable "region" {
  description = "GCP Region (기본: 서울)"
  type        = string
  default     = "asia-northeast3"
}

variable "bucket_name" {
  description = "Cloud Storage bucket name"
  type        = string
  nullable    = false
  
  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9-]*[a-z0-9]$", var.bucket_name))
    error_message = "Bucket name must be lowercase letters, numbers, and hyphens only."
  }
}

variable "environment" {
  description = "Environment name (production/staging/development)"
  type        = string
  default     = "production"

  validation {
    condition     = contains(["production", "staging", "development"], var.environment)
    error_message = "Environment must be production, staging, or development."
  }
}

variable "firebase_admin_members" {
  description = "List of email addresses to grant Firebase Admin role"
  type        = list(string)
  default     = ["maintain0404@gmail.com"]
}
