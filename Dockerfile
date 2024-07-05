ARG PYTHON_VERSION=3.10.5
ARG NGINX_VERSION=1.23.0
FROM python:${PYTHON_VERSION}-alpine

WORKDIR /usr/src/app


RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY config/nginx.conf /etc/nginx/conf.d


EXPOSE 8000 80


CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application & nginx -g 'daemon off;'"]