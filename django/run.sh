python manage.py makemigrations --settings=config.settings.development_sqlite
python manage.py migrate --settings=config.settings.development_sqlite
python manage.py runserver --settings=config.settings.development_sqlite