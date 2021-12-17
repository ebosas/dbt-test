output "pg_endpoint" {
  description = "Base URL for API Gateway stage"
  value       = aws_db_instance.postgres.endpoint
}