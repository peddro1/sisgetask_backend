# Makefile

SERVICE_NAME = sisgetask_backend

up:
	docker compose up -d

ub:
	docker compose up --build -d

down:
	docker compose down

restart: down up

logs:
	docker compose logs -f

migrate:
	docker compose exec $(SERVICE_NAME) python manage.py migrate

makemigrations:
	docker compose exec $(SERVICE_NAME) python manage.py makemigrations

createsuperuser:
	docker compose exec $(SERVICE_NAME) python manage.py createsuperuser

shell:
	docker compose exec $(SERVICE_NAME) python manage.py shell

psql:
	docker compose exec psql psql -U $$(grep POSTGRES_USER dotenv_files/.env | cut -d '=' -f2 | tr -d '"') -d $$(grep POSTGRES_DB dotenv_files/.env | cut -d '=' -f2 | tr -d '"')
	
collectstatic:
	docker compose exec $(SERVICE_NAME) python manage.py collectstatic --noinput

docker-clean-all:
	docker ps -a -q | xargs -r docker rm -f
	docker images -q | xargs -r docker rmi -f
	docker volume ls -q | xargs -r docker volume rm
	docker network ls -q | xargs -r docker network rm

