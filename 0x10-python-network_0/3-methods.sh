#!/bin/bash
# script that takes in URL & displays all HTTP methods the server will accept
curl -X GET $1
