## Testing dbt

Launch Postgres in a local container:

```bash
docker compose up
```

Connect to the database:

```bash
docker run -it --rm \
    --network dbt_network \
    postgres:14-alpine \
    psql -h postgres -U postgres -d dbt
```
