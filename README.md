# Haproxy test

Experiment playing around with haproxy for routing

## Setup steps

You will need ha proxy installed.  On mac:  
`brew install haproxy`

We want to start ha proxy with the  config file we have supplied:
`haproxy -f haproxy.cfg`

This will run on port 8000.  So visit http://127.0.0.1:8000.  At the moment the only file that exists is at: http://127.0.0.1:8000/static-assets/test.txt

In this example so far we route all requests to an s3 bucket for now.

## Todo

Add in other routes and some test backends to play around with haproy routing.

