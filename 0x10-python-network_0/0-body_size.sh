#!/bin/bash
# the script sends a request to that URL displays the size of the response body

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1
response=$(curl -sI "$URL")
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r\n')

echo "$content_length"
