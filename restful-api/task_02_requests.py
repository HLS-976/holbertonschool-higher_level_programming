#!/usr/bin/python3
"""This module provides a thing"""
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = response.status_code
    print(f"Status code: {status_code}")
    if status_code == 200:
        json_data = response.json()
        for element in json_data:
            print(element['title'])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    status_code = response.status_code
    list_of_data = []
    if status_code == 200:
        json_data = response.json()
        for element in json_data:
            list_of_data.append({'id': element['id'], 'title': element['title'], 'body': element['body']})
    with open('posts.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        for elem in list_of_data:
            writer.writerow(elem)

fetch_and_print_posts()
fetch_and_save_posts()