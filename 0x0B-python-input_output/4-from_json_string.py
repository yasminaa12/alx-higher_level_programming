#!/usr/bin/python3
"""this module determines a JSON-to-object function."""

import json 


def from_json_string(my_str):
    """returns the python object protrayal of a JSON string"""
    return json.loads(my_str)
