#!/bin/bash
# Sending a GET request and storing the response body in a variable
echo -n curl -s $1 | wc -c

