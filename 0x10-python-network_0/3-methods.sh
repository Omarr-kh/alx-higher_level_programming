#!/bin/bash
# displays all http mehtods
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
