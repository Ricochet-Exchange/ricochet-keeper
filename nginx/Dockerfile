FROM nginx:latest
RUN openssl req -new -newkey rsa:2048 -days 3650 -nodes -x509 \
    -subj '/CN=airflow-webserver' \
    -keyout /etc/ssl/private/airflow-webserver.key \
    -out /etc/ssl/certs/airflow-webserver.crt
RUN rm /etc/nginx/conf.d/default.conf
COPY airflow.conf /etc/nginx/conf.d/airflow.conf
