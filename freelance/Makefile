migrate:
	python manage.py makemigrations && python manage.py migrate

migrate_fake:
	python manage.py makemigrations && python manage.py migrate --fake

run:
	python manage.py runserver 8002

loaddata:
	python manage.py loaddata fixtures/initial_data.json

dumpdata:
	python manage.py dumpdata --indent 4 --exclude contenttypes --exclude auth.Permission > fixtures/initial_data.json