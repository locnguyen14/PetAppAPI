TODO:

1. Document how to run the app with docker. This include:

- build the image: docker-compose build
- run the container: docker-compose run <service_name> <django_commands>
  - Example: docker-compose run app python manage.py shell
- migrate the database: docker-compose run app python manage.py migrate
  - You can access the postgres db with: (inside the note)

2. Document how to run the app locally:

- Need to communicate with another device --> expose the server with the ip machine. Example, if your machine IP is x.x.x.x and the app is running on port 8000 --> python manage.py runserver x.x.x.x:8000
