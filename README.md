## Testing dbt

Launch Postgres in a local container:

```bash
docker compose up
```

Connect to the local database:

```bash
docker run -it --rm \
    --network dbt_network \
    postgres:14-alpine \
    psql -h postgres -U postgres -d dbt
```

Create a Postgres database on AWS RDS. Make sure to add a password in `secret.tfvars`.

```bash
terraform apply -var-file="secret.tfvars"
```

Connect to a remote database:

```bash
docker run -it --rm \
    postgres:14-alpine \
    psql -h <pg_endpoint> -p 5432 -U postgres -d dbt -W
```
