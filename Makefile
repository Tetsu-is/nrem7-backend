# TODO: 後で精査する
setup:
	make install
	cp .env.example .env

install:
	docker-compose exec web pip install -r requirements.txt

migrate:
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py superuser

up:
	docker-compose up

enter:
	docker-compose exec web /bin/sh

enter-db:
	docker-compose exec db /bin/sh
