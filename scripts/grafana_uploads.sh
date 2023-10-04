#!/bin/bash

docker compose run gdg backup connection upload
docker compose run gdg backup dashboard upload
docker compose run gdg backup libraryelements upload