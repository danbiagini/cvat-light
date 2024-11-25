#!/bin/bash

docker compose -f docker-compose.yml -f docker-compose.external_db.yml -f light-overlay/docker-compose-light.yml up -d
