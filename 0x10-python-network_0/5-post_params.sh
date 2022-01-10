#!/bin/bash
# POST request and displays the body of the response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
