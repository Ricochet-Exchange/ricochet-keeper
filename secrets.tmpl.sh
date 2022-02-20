#!/bin/bash
sed -i 's/postgresql_strong_password/${PG_PWD}/' docker-compose.yml
sed -i 's/fernet_strong_password_here/${FERNET_KEY}/' docker-compose.yml
sed -i 's/airflow_gui_password/${AIRFLOW_PASSOWRD}/' docker-compose.yml
