resource "aws_db_instance" "postgres" {
  allocated_storage      = 20
  max_allocated_storage  = 21
  storage_type           = "gp2"
  engine                 = "postgres"
  engine_version         = "12.8"
  instance_class         = "db.t2.micro"
  name                   = "dbt"
  username               = var.db_username
  password               = var.db_password
  vpc_security_group_ids = [aws_security_group.postgres.id]
  multi_az               = false
  publicly_accessible    = true
  skip_final_snapshot    = true
}

resource "aws_security_group" "postgres" {
  name        = "postgres"
  description = "Postgre security group"

  ingress {
    description = "Access from anywhere"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}