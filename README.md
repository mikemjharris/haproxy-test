# Haproxy test

Experiment playing around with haproxy for routing

## Setup steps

Runs in docker container run:
`docker-compose build && docker-compose up`

The current setup is to show the python simple server doesn't send back right headers/protocol (believe it responds with http 1.0) so haproxy doesn't gzip the response.

Python simple server backend with haproxy trying to gzip - doesn't work
http://localhost:8002/gzip-broke/test.txt

Node server backend with haproxy trying to gzip - works
http://localhost:8002/gzip-broke/test.txt

S3 backend with haproxy trying to gzip - works
http://localhost:8002/gzip-yes/test.txt

S3 backend with haproxy not trying to gzip - works as expected (no gzip)
http://localhost:8002/gzip-yes/test.txt
