ARG NGINX_VERSION=1.23.0

FROM nginx:${NGINX_VERSION}-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY config/nginx.conf /etc/nginx/conf.d
