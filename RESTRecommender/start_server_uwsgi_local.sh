#!/bin/bash

# Start the server and listen on localhost port 8080
uwsgi --ini resources/config/config-local.ini

# To call the webservice: curl http://localhost:8080/recommender

