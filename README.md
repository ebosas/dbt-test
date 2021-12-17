## Testing dbt

### Locally

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

### On AWS

Add a password in `secret.tfvars`. Then create a Postgres database in AWS RDS.

```bash
cd deployments
terraform apply -var-file="secret.tfvars"
```

Connect to a remote database:

```bash
docker run -it --rm \
    postgres:14-alpine \
    psql -h <pg_endpoint> -p 5432 -U postgres -d dbt -W
```

### dbt

Commands:

```bash
dbt debug
dbt seed
dbt run
dbt test
dbt docs generate
dbt docs serve
```
