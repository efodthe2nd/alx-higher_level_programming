#!/bin/bash
# POST request to the passed URL, amd displays the body of the response
curl -sX POST -F "email=test@gmail.com" -F "subject=I will always be here for PLD" "$1"
