#!/usr/bin/python3
"""
This module provides a thing
"""
import requests
import csv


def fetch_and_print_posts():
    """
    This function fetch data and print it
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = response.status_code
    print(f"Status code: {status_code}")
    if status_code == 200:
        json_data = response.json()
        for element in json_data:
            print(element['title'])


def fetch_and_save_posts():
    """
    This function fecth data and save some information
    on a list and save on csv format
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = response.status_code
    if status_code == 200:
        list_of_data = []
        json_data = response.json()
        for element in json_data:
            list_of_data.append(
                {'id': element['id'],
                 'title': element['title'],
                 'body': element['body']
                 })
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for elem in list_of_data:
                writer.writerow(elem)
