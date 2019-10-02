# Grab Tweets

## To Run the background tasks the follwing must be done
    - create a virtual environment and install app dependencies
    - create a .env file at the root of the project
    - check the .env_sample for the required environmental variables
    - go to the settings.py folder and uncomment the settings for postgres if you don't want to use sqllite3
    - run migrations with `python manage.py migrate`
    - start redis with `redis-server`
    - start celery with `celery worker -A getTweeterTips --loglevel=info --pool=solo`
    - start celery beat with `celery -A getTweeterTips beat -l info`

## To perform the CRUD functionalities of the app
    - run the server with `python manage.py runserver 5000`
    - make sure your developer app is set up on twitter since this app is not hosted
    - go to the login page `localhost:5000/login/` to login with twitter
    - you will be redirected to `localhost:5000/api/tips/`to interact with the app

## To perform search functionalities
    - localhost:5000/api/tips/?search=<what you want to search>&search_fields=<model fields to be searched>

## To logout of the application
    - localhost:5000/logout/
