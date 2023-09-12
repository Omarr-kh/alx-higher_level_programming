#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function that returns an object repres by json."""
import json


def from_json_string(my_str):
    """Return object representation of a JSON string."""
    return json.loads(my_str)
