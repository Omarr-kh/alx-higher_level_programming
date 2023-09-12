#!/usr/bin/python3
"""Defines a function that read JSON from file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
