
# RESTRecommender

This Python code implements a Falcon REST API, responsible for:

- Accepting REST requests (using Falcon)
- Applying the pertinent recommender algorithm
- Returning a JSON with the response


## System Requirements ##

- Python >3
- Numpy
- Falcon
- uwsgi

This will install all the requirements for python 3:
> pip3 install -r requirements.txt


## Running uWSGI server locally ##

Run a local server:
> uwsgi --http :8080 --wsgi-file scr_start_listening.py --callable recommender_app --master

How to run the server for the RESTRecommender
> sh start_server_uwsgi_local.sh

This starts the server loading the file resources/config/config-local.ini , which includes all the configuration variables to run the server in your local machine.


## Send a http request ##

To send a request to the server run in terminal (or in a browser) a URL such as:

curl -H "Content-Type: application/json" -X POST -d '{"type": "recommendation","user_id": 1,"state_user":"FL","timestamp" : 1591514264000}' http://localhost:8080/recommender



### Test Coverage ###

For monitoring the test coverage locally, we can use [Coverage.py](https://coverage.readthedocs.io)

To install the coverage tool:
```bash
pip install coverage
```

To print the coverage for the code
```bash
coverage run --source=REST  -m unittest discover unit_tests -p "*_unittest.py" 

coverage report -m
```

To view the project coverage online, please visit [CodeCov](https://codecov.io/)
