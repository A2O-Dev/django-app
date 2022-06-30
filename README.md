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

3. Generate secret key

Generate with the next command

```shell
docker compose exec app python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

The output save in .env file in the next variable

```
APP_KEY
```

4. Migrate database and seed

To Migrate

```shell
docker compose exec app python manage.py migrate
```

To Seed

```shell
docker compose exec app python manage.py seeder
```

5. Generate static files

```shell
docker compose exec app python manage.py collectstatic
```

6. Create a superuser

```shell
docker compose exec app python manage.py createsuperuser
```
