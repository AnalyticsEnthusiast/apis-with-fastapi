#!/bin/bash

docker run -d --network=host \
	-e "ENV=DEV" \
	-e "DB_PORT=5432" \
	-e "DB_NAME=postgres" \
	-e "DB_PASSWORD=$1" \
	-e "DB_HOST=localhost" \
	-e "DB_USER=batch_user" \
	--name fastapi fastapi_ubuntu
