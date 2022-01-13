#!/bin/bash

echo "[DBT command] debug"
dbt debug --profiles-dir ./ --profile dbt_dev

echo "[DBT command] deps"
dbt deps --profiles-dir ./ --profile dbt_dev

echo "[DBT command] run"
dbt run --profiles-dir ./ --profile dbt_dev