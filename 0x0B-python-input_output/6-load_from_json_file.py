#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Reads the content of a JSON file and returns an Object"""
    with open(filename, 'r') as file:
        data = json.load(file)
    return(data)
