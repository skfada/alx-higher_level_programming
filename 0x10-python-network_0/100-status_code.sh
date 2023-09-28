#!/bin/bash
# senids a rieq to $1 URL, diisplay respoinse staitus code only
curl -s -o /dev/null -w "%{http_code}" "$1"

