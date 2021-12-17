variable "aws_region" {
  description = "AWS region for all resources"
  default     = "eu-west-1"
  type        = string
}

variable "db_username" {
  description = "Postgres username"
  type        = string
}

variable "db_password" {
  description = "Postgres password"
  type        = string
  sensitive   = true
}
