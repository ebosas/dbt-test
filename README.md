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

Create an SSM parameter for the Postgres password with the name `/dbt/PostgresPassword` and type `SecureString`. Then deploy the CloudFormation stacks. First, the VPC.

```bash
cd deployments
aws cloudformation create-stack --stack-name db-vpc --template-body file://vpc.yaml
```

Once done, deploy the database stack.

```bash
aws cloudformation create-stack --stack-name db-postgres --template-body file://db.yaml
```

Connect to a remote database:

```bash
docker run -it --rm \
    postgres:14-alpine \
    psql -h <pg_endpoint> -p 5432 -U postgres -d dbt -W
```
