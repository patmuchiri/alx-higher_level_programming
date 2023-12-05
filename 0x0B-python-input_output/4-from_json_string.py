#!/usr/bin/python3
"""Defines a JSON-to-Object(string) function"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) JSON string."""
    return json.loads(my_str)
