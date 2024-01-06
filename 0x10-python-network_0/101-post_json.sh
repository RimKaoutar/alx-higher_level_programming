#!/bin/bash
# Send a JSON POST request and display the body of the response
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
