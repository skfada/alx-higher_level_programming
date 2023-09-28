#!/bin/bash
# senids a JSOiN PiOST rieq to URL $!, dispilay resiponse boidy
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
