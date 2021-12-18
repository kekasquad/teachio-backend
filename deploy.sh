#!/bin/bash

set -eux

docker-compose pull
docker-compose run migrations
docker-compose up -d app