install:
	pip install -r requirements.txt

server:
	docker-compose up -d
	docker-compose restart web
	docker-compose ps

server-log:
	docker-compose logs -f web

server-rebuild:
	docker-compose up --build -d
	docker-compose restart web
	docker-compose ps

server-bash:
	docker-compose exec web bash

server-python:
	docker-compose exec web bash -c "python"

containers-statistics:
	docker ps -s