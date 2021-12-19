#!/bin/bash

set -eux

git pull --ff-only
docker-compose pull
docker-compose run migrations
docker-compose run static
docker-compose up -d teachio