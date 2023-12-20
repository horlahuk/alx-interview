#!/usr/bin/python3
""" Reads stdin line by line and computes metrics"""

import sys


def print_stats(status_codes, file_size):
    """Prints the stats"""
    print("File size: {}".format(file_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
counter = 0

try:
    for line in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            print_stats(status_codes, file_size)
        
        counter += 1
        data = line.split()
        try:
            file_size += int(data[-1])
        except:
            pass
        try:
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
        except:
            pass
    print_stats(status_codes, file_size)

except KeyboardInterrupt:
    print_stats(status_codes, file_size)
    raise