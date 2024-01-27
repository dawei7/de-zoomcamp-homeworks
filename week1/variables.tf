variable "credentials" {
  description = "Path to the credentials file"
  type        = string
  default     = "./keys/my-creds.json"
}


variable "project" {
  description = "Project ID"
  type        = string
  default     = "de-zoomcamp-412423"
}

variable "location" {
  description = "Project Location"
  type        = string
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  type        = string
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket name"
  type        = string
  default     = "terraform-demo-777777788-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  type        = string
  default     = "STANDARD"
}