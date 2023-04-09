0. General command to run docker with docker-compose:

   - docker-compose run <service_name> <django_commands>

1. Running Pet App API with Docker:

   For ease of development, this Django application is containerized with Docker and can be run with of couplfe of task:

   - Clone the application
   - Open the application in a command window/terminal
   - Run `docker-compose build`--> build the image
   - Run `docker compose up` --> run the container
   - Run `docker-compose run app python manage.py migrate` --> set up the schema for postgres database
   - Run `docker-compose run app python manage.py shell` --> interact with Django server and seed in some data

2. How to expose API to other machine (beside your own computer):

   - Run `pip install -r requirements.txt` to install all dependencies on your machine
   - I want to test my app on my own personal IPhone and was running into a this particular networking issues: the main communication method is WIFI and the iOS device could not talk to my Window laptop because Apple device might not be able to recognize **localhost:8000** or **127.0.0.1:8000** due to different OS architechture. As a result, I need to expose the API via the IP address of the Wifi router:
   
     - Search for the router IP address in the command line with : `ipconfig`. Say the IP config is: 123.123.4.1
     - Expose your API with Django command: `python app\manage.py runserver 123.123.4.1:8000`
     
   - If your API is run/hosted on a Mac, simply run: `python app\manage.py runserver`
