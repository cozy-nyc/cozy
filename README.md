#exchange

### Requirements
* [Docker Engine](https://docs.docker.com/engine/installation)
* [Docker Compose](https://docs.docker.com/compose/install)

### Stack
* Postgres
* Django
* Webpack + React
* Mocha for js testing
* Pytest for python testing

### Setup and customize

1. Edit the environement variables
` touch .env`
2. Create env/dev with the following values filled

```
SECRET_KEY=[secret-key]
DEBUG=true
DJANGO_SETTINGS_MODULE=django_config.settings.local
ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0
DATABASE_URL=postgres://django:[password]@localhost:5432/[project-name]

MAILGUN_API_KEY=[mailgun-api-key]
MAILGUN_DEFAULT_FROM_EMAIL=[email]

POSTGRES_PASSWORD=[password]
POSTGRES_USER=django
POSTGRES_DB=[project-name]

EMAIL_PORT=1025
EMAIL_HOST=localhost
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DEFAULT_FROM_EMAIL=[email]
```

Finally, build and start the docker containers:

```
./bin/develop
```

### Run Django commands

```
./bin/django [command]
./bin/django createsuperuser
./bin/django makemigrations [app_name]
```
