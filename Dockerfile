ARG PYTHON_VERSION=3.10.5

FROM python:${PYTHON_VERSION}-alpine

WORKDIR /usr/src/app

RUN apk add -U --no-cache nginx supervisor

RUN pip install --upgrade pip
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Generate Static files
RUN python manage.py collectstatic --noinput

# Setting supervisord
RUN mkdir -p /var/log/supervisor
COPY --chmod=0777 docker/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Setting nginx
COPY --chmod=0777 docker/nginx/nginx.conf /etc/nginx/http.d/default.conf

EXPOSE 80

## Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
