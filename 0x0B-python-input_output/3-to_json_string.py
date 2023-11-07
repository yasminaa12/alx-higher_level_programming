#!/usr/bin/python3
"""this module determines a string-to-json function"""
 import json


 def to_json_string(my_obj):
     """a string oject's json reprsentation is returned."""
     return json.dumps(my_obj)
