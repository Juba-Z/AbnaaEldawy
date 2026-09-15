import os
from flask import Flask, render_template, request, jsonify
import pyodbc
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_SERVER = os.getenv('DB_SERVER', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'products_db')
DB_USER = os.getenv('DB_USER', 'sa')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')

conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    f'SERVER={DB_SERVER};'
    f'DATABASE={DB_NAME};'
    f'UID={DB_USER};'
    f'PWD={DB_PASSWORD};'
    'TrustServerCertificate=yes;'
)

def get_db_connection():
    return pyodbc.connect(conn_str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def search_products():
    search = request.args.get('search', '')
    conn = get_db_connection()
    cursor = conn.cursor()
    if search:
        query = """
            SELECT ID, Product_Name, Selling_Price, Purchase_Price
            FROM products
            WHERE Product_Name LIKE ?
            ORDER BY Product_Name
        """
        cursor.execute(query, f'%{search}%')
    else:
        query = "SELECT ID, Product_Name, Selling_Price, Purchase_Price FROM products ORDER BY Product_Name"
        cursor.execute(query)
    rows = cursor.fetchall()
    products = [
        {
            'id': row[0],
            'name': row[1],
            'selling_price': row[2],
            'purchase_price': row[3]
        } for row in rows
    ]
    conn.close()
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        UPDATE products
        SET Product_Name=?, Selling_Price=?, Purchase_Price=?
        WHERE ID=?
    """
    cursor.execute(query, data['name'], data['selling_price'], data['purchase_price'], product_id)
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM products WHERE ID=?"
    cursor.execute(query, product_id)
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    if not data or not all(k in data for k in ('name', 'selling_price', 'purchase_price')):
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO products (Product_Name, Selling_Price, Purchase_Price, Discount)
        VALUES (?, ?, ?, 0)
    """
    cursor.execute(query, data['name'], data['selling_price'], data['purchase_price'])
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True) 