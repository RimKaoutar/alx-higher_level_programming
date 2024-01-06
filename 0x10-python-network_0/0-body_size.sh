#!/bin/bash
# gets the length of the body of an html get request
curl -sI "$1" | grep -i Content-Length | awk '{print$2}'
