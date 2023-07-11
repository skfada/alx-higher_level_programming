#!/usr/bin/python3
"""
this is the read_file function
"""


def read_file(filename=""):
    """""reads a text in file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
