#!/usr/bin/python3
"""This module determines a string-to-JSON function"""
import json


def to_json_string(my_obj):
    """a string object's JSON representation is returned."""
    return json.dumps(my_obj)
