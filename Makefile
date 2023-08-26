# TODO: 後で精査する
setup:
	make install
	cp .env.example .env

install:
	pip install -r requirements.txt

start:
	python manage.py runserver

migrate:
	python manage.py migrate
	python manage.py superuser

up:
	docker-compose up

enter:
	docker-compose exec web /bin/sh

make-exec-migrate:
	docker-compose exec web python manage.py migrate
