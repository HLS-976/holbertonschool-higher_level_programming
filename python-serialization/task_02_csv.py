#!/usr/bin/python3
"""
This module provides a function that convert
csv data into json and save it on the file
"""
import csv
import json
import os


def convert_csv_to_json(csv_filename):
    """
    This function convert the content of csv file into json
    and save it on the another file
    """

    try:
        if not os.path.exists(csv_filename):
            raise FileNotFoundError("File not found")

        with open(csv_filename, 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        with open('data.json', 'w', encoding='utf8') as f:
            json.dump(data, f, indent=4)

        return True
    except FileNotFoundError as e:
        print(e)
        return False
