#!/usr/bin/python3
"""functions that returns json """
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object."""
    return json.dumps(my_obj)
