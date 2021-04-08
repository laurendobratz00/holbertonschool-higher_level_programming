#!/bin/bash
# a Bash script that sends a request to that URL,and displays the size of body
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
