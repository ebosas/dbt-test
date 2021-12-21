#!/bin/bash

echo "[dbt command] debug"
dbt debug --profiles-dir ./ --profile dbt_dev

echo "[dbt command] run"
dbt run --profiles-dir ./ --profile dbt_dev