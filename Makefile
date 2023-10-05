.PHONY: up down format shell

up:
	docker compose up

down:
	docker compose down --rmi local --remove-orphans --volumes

shell:
	docker compose exec api bash

revision:
	alembic revision --autogenerate -m $@

format:
	isort .
	black .
