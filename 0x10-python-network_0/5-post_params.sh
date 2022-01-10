#!/bin/bash
# POST request and displays the body of the response
curl -sd "$1" -X POST "email=hr@holbertonschool.com&subject=I will always be here for PLD"
