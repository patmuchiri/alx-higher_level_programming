#!/usr/bin/bash
def simple_delete(a_dictionary, key=""):
    if isinstance (key, str) and key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
