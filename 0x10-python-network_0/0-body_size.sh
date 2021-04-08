#!/bin/bash
curl -sI -X "$1" | grep -i Content-Length | awk '{print $2}'
