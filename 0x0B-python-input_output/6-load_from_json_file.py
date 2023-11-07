#!/usr/bin/python3
"""This module determines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """uses a given JSON file to produce a Python object."""

    with open(filename) as f:
        return json.load(f)
