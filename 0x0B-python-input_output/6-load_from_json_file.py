#!/usr/bin/python3
"""
the function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    """it creiate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
