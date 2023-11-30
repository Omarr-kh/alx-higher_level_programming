#!/bin/bash
# sends request to a url and displays the size of the body
curl -s "$1" | wc -c
