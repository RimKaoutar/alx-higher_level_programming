#!/bin/bash
# Send a request and display only the status code of the response
curl -s "$1" -w "%{http_code}" -o /dev/null
