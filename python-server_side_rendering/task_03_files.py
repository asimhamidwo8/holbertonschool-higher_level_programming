#!/usr/bin/python3
"""Flask application that displays product data from JSON, CSV, or SQL."""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filepath):
    """Read and return product data from a JSON file."""
    with open(filepath, 'r') as file:
        return json.load(file)


def read_csv(filepath):
    """Read and return product data from a CSV file."""
    products = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    """Read and return product data from the SQLite database."""
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    """Render the product list, filtered by source and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        try:
            data = read_sql()
        except sqlite3.Error:
            return render_template('product_display.html',
                                    error="Error retrieving data from database")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                    error="Invalid product ID")

        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html',
                                    error="Product not found")
        data = filtered

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
