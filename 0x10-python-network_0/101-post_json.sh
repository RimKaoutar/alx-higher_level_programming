#!/bin/bash
# Send a JSON POST request and display the body of the response
curl -s "$1" -X POST -H "Content-Type: application/json" -d "@$2"
