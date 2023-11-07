#!/usr/bin/python3
"""This module determines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """uses the JSON format to write an object to a text file."""

    with open(filename, "w") as f:
        json.dump(my_obj, f)
