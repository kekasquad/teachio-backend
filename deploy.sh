#!/bin/bash

set -eux

git pull
docker-compose build
docker-compose run migrations
docker-compose up -d app