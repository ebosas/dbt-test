#!/bin/bash

dbt debug --profiles-dir ./
dbt run --profiles-dir ./