#!/bin/bash
# Takes in an URL and displays all HTTP methods the server will accept
curl -svX OPTIONS "$1"
