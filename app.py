import os
import re
import sqlite3
import tempfile
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env_file = os.path.join(BASE_DIR, '.env')
if os.path.exists(env_file):
    try:
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"\''))
    except Exception:
        pass

app = Flask(__name__)

DB_PATH = os.getenv('DB_PATH', os.path.join(BASE_DIR, 'products.db'))
ADMIN_PIN = os.getenv('ADMIN_PIN', '1234')

def normalize_arabic(text):
    if not text:
        return ""
    # Remove tashkeel (diacritics) & tatweel
    text = re.sub(r'[\u064B-\u0652\u0640]', '', text)
    # Normalize Alef forms (أ, إ, آ, ٱ -> ا)
    text = re.sub(r'[أإآٱ]', 'ا', text)
    # Normalize Ta Marbouta & Ha (ة -> ه)
    text = re.sub(r'ة', 'ه', text)
    # Normalize Ya & Alef Maqsura (ى -> ي)
    text = re.sub(r'ى', 'ي', text)
    return text.strip().lower()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.create_function("NORMALIZE_ARABIC", 1, normalize_arabic)
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Discount REAL DEFAULT 0,
            Purchase_Price REAL DEFAULT 0,
            Selling_Price REAL DEFAULT 0,
            Product_Name TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()


# ─── PDF Parsing ────────────────────────────────────────────

def fix_reversed_text(raw_text):
    if not raw_text:
        return ""
    rev = raw_text[::-1].strip()
    return re.sub(r'[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*', lambda m: m.group(0)[::-1], rev)

def parse_pdf(path):
    import pdfplumber
    products = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            for line in text.split("\n"):
                line = line.strip()
                match = re.search(r"^([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)\s+(.+)$", line)
                if match:
                    products.append({
                        "discount": float(match.group(1)),
                        "purchase_price": float(match.group(2)),
                        "selling_price": float(match.group(3)),
                        "name": fix_reversed_text(match.group(4).strip())
                    })
    return products


# ─── Routes ─────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products', methods=['GET'])
def search_products():
    search = request.args.get('search', '').strip()
    conn = get_db_connection()
    if search:
        norm = normalize_arabic(search)
        words = norm.split()
        if words:
            clauses = ["NORMALIZE_ARABIC(Product_Name) LIKE ?" for _ in words]
            params = [f'%{w}%' for w in words]
            sql = f"SELECT ID, Product_Name, Selling_Price, Purchase_Price FROM products WHERE {' AND '.join(clauses)} ORDER BY Product_Name"
            rows = conn.execute(sql, params).fetchall()
        else:
            rows = []
    else:
        rows = conn.execute(
            "SELECT ID, Product_Name, Selling_Price, Purchase_Price FROM products ORDER BY Product_Name"
        ).fetchall()
    conn.close()
    products = [{'id': r['ID'], 'name': r['Product_Name'], 'selling_price': r['Selling_Price'], 'purchase_price': r['Purchase_Price']} for r in rows]
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400
    conn = get_db_connection()
    conn.execute(
        "UPDATE products SET Product_Name=?, Selling_Price=?, Purchase_Price=? WHERE ID=?",
        (data['name'], data['selling_price'], data['purchase_price'], product_id)
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM products WHERE ID=?", (product_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    if not data or not all(k in data for k in ('name', 'selling_price', 'purchase_price')):
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO products (Product_Name, Selling_Price, Purchase_Price, Discount) VALUES (?, ?, ?, 0)",
        (data['name'], data['selling_price'], data['purchase_price'])
    )
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})


# ─── Admin: PDF Upload ─────────────────────────────────────

@app.route('/api/admin/update-pdf', methods=['POST'])
def admin_update_pdf():
    pin = request.form.get('pin', '')
    if pin != ADMIN_PIN:
        return jsonify({'status': 'error', 'message': 'رمز الدخول غير صحيح'}), 403

    pdf_file = request.files.get('pdf')
    if not pdf_file or not pdf_file.filename.lower().endswith('.pdf'):
        return jsonify({'status': 'error', 'message': 'يرجى اختيار ملف PDF صالح'}), 400

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    try:
        pdf_file.save(tmp.name)
        tmp.close()

        products = parse_pdf(tmp.name)
        if not products:
            return jsonify({'status': 'error', 'message': 'لم يتم العثور على أصناف في الملف'}), 400

        conn = get_db_connection()
        conn.execute("DELETE FROM products")
        for p in products:
            conn.execute(
                "INSERT INTO products (Product_Name, Selling_Price, Purchase_Price, Discount) VALUES (?, ?, ?, ?)",
                (p['name'], p['selling_price'], p['purchase_price'], p['discount'])
            )
        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'count': len(products)})
    finally:
        os.unlink(tmp.name)


if __name__ == '__main__':
    app.run(debug=True)