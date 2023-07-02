#!/bin/bash
# Bash Script that SEND POSt and displaying body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
