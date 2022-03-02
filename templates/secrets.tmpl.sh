#!/bin/bash
sed -i 's/postgres_password/${PG_PWD}/' docker-compose.yml
sed -i 's#fernet_password#${FERNET_KEY}#' docker-compose.yml
sed -i 's/airflow_password/${AIRFLOW_PASSWORD}/' docker-compose.yml
