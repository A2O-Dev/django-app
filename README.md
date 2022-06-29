# Django App Demo

Application to serve product catalog

## Installing

1. Copy environment file (and edit to your values)

```shell
cp .env.example .env
```

2. Up containers

```shell
docker compose up -d
```

3. Migrate database

```shell
docker compose exec app python manage.py migrate
```
