#!/usr/bin/python3
"""
it contains the json str function
"""

import json


def from_json_string(my_str):
    """returns an object rep by a JSON string"""
    return json.loads(my_str)
