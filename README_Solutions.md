# Global Test
## Description
Solution was built using Django and has also been containerized using Docker & Docker-Compose with a PostgreSQL database service to store data. 

Further, to prepopulate data for convenience of your review django-extensions was utilsed to upload relevant data and can be found in the "scripts" module. Model serializers have been included for conversion between content types. To ensure the database functionality, "management commands" (wait_for_db found in core/management/commands) were developed to wait for the database to be ready before use. 


Upon the below install and run command, the code will automatically read and serialize the json track data, as well as run the server.
To upload an xml file, please access /upload endpoint, to view countries please use /book and /admin to delete any records.
There were challenges mostly in containerization, as i did not expect django rest framework to have a few bugs in process.

# Installation
```
docker build .
docker-compose build

set up admin user:
docker-compose run app sh -c "python manage.py createsuperuser"

to clear database:
docker-compose run app sh -c "python manage.py flush"

```

# Run
```
docker-compose up

to install and run simultaneously:
docker-compose up --build
```

# Endpoints for solution (with brief description of use)
```
- Fetch a single track: - api/fetch_track/ (Please append track id to url)
- Create a new track: - /api/add_track/ (Please use form at link)
- List the first 100 most recently played tracks - /api/last_played/ (Access link)
- Filter tracks by name: - /api/filter_track/ (Upon accessing endpoint, please click Filters button to filter track by name)
- Bonus: - /api/filter_artist/ (Please enter artists in url seperated by commas after appending "?search=")

main api endpoints:
- /api

```

# Notes
There was an error unforseen using the filter in the api/filter_artist/ endpoint which made the button disappear. I would have liked to include an html file with a search field to properly handle this, but the assumption made here was the focus was on use of the DjangoRestAPI. Ideally, would have liked to test the Api endpoints if there was more time, including mocking the wait_for_db command.
