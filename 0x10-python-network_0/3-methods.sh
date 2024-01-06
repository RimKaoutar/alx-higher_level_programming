#!/bin/bash
# send an OPTIONS request and display the allowed HTTP methods
curl -sI "$1" | awk -F ": " '/Allow/ {print $2}'
