# News

## Local development

Start PostgreSQL in Docker:

```bash
sudo docker run --name postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
```

Run application:

```bash
$ export FLASK_APP=news
$ export FLASK_ENV=development
$ flask run
```

Database:
```bash
$ flask db migrate
$ flask db upgrade
```
See: https://flask-migrate.readthedocs.io/en/latest/

```bash
sudo docker exec -it postgres-db bash
su postgres
psql
\conninfo
\q
``` 

enter data:
```bash
$ curl -X POST http://127.0.0.1:5000/feeds -H 'Content-Type: application/json' -d '{"url":"http://feeds.nos.nl/nosnieuwsalgemeen"}'

``` 