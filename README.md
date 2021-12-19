# teachio-backend

## Production deployment

```shell
docker-compose up -d --build
docker-compose run migrations
```

## Celery

### Quick start

Development:

```shell
celery -A teachio_backend worker -B --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

Production:

```shell
celery -A teachio_backend worker
celery -A teachio_backend beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

### Flower

```shell
celery -A teachio_backend flower
```
