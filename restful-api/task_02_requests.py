#!/usr/bin/env python3
"""
task_02_requests.py

Fetch posts from JSONPlaceholder, print titles and status code, and save posts to CSV.
"""
from typing import List, Dict
import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts() -> None:
    """Fetch all posts from JSONPlaceholder and print status code and titles.

    Prints a line like "Status Code: 200" followed by the titles of all posts,
    one per line.
    """
    try:
        resp = requests.get(URL, timeout=10)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    print(f"Status Code: {resp.status_code}")

    if resp.status_code != 200:
        return

    try:
        posts = resp.json()
    except ValueError:
        print("Failed to parse JSON response.")
        return

    if not isinstance(posts, list):
        print("Unexpected JSON structure: expected a list of posts.")
        return

    for post in posts:
        title = post.get("title", "")
        print(title)


def fetch_and_save_posts(csv_filename: str = "posts.csv") -> None:
    """Fetch all posts from JSONPlaceholder and save id, title, body to a CSV file.

    The CSV will have columns: id, title, body. The file is written using
    newline='' and utf-8 encoding for cross-platform compatibility.
    """
    try:
        resp = requests.get(URL, timeout=10)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    print(f"Status Code: {resp.status_code}")

    if resp.status_code != 200:
        return

    try:
        posts = resp.json()
    except ValueError:
        print("Failed to parse JSON response.")
        return

    if not isinstance(posts, list):
        print("Unexpected JSON structure: expected a list of posts.")
        return

    rows: List[Dict[str, object]] = []
    for post in posts:
        rows.append({
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        })

    fieldnames = ["id", "title", "body"]
    try:
        with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    except OSError as e:
        print(f"Failed to write CSV file: {e}")


if __name__ == "__main__":
    # allow ad-hoc manual testing
    fetch_and_print_posts()
    fetch_and_save_posts()
