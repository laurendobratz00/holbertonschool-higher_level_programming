#!/bin/bash
# a Bash script that sends a request to that URL,and displays the size of body
curl -sI $URL | grep -i Content-Length | awk '{print $2}'
