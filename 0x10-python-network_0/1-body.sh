#!/bin/bash
# a script that sends a GET request to the URL,and displays the body of response
curl -sI -X GET -H $1
