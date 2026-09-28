# Abnaa ElDawy - Product & Price Catalog
### أبناء الضوى للتجارة والتوزيع

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![AI Assisted](https://img.shields.io/badge/Developed%20with-AI%20Pair%20Programming-D4AF37?style=for-the-badge&logo=sparkles&logoColor=black)](https://github.com)

A modern, high-performance product price catalog and management system designed for **Abnaa ElDawy Trading & Distribution**. Built with Python (Flask) and SQLite, featuring a luxury Dark & Gold glassmorphism interface, integrated PDF price parsing, intelligent Arabic text normalization, and an Android mobile app.

---

## ✨ Features | المميزات الرئيسية

- **⚡ Instant Real-Time Search:** Search products by Arabic name or number with smooth live rendering.
- **🧠 Smart Arabic Search Normalization:** Custom intelligent normalization engine handling all Arabic character variations (`أ / إ / آ / ا`, `ة / ه`, `ى / ي`), kashida, and diacritics.
- **💎 Dark & Gold Luxury Interface:** Glassmorphism UI with micro-animations, Cairo Arabic typography, and mobile-first responsive design.
- **📄 Bulk Price Update via PDF:** Upload price lists in PDF format directly from the browser; automatically parses items and fixes reversed Arabic text and numbers.
- **🔐 PIN-Protected Admin Actions:** Secure administrative endpoints protected by a customizable PIN.
- **✏️ Quick Inline Editing & Management:** Add, update prices, or delete items directly from interactive cards.
- **📱 Android App (APK):** Standalone Android app wrapper (`AbnaaElDawy.apk`) that runs without browser bars.
- **☁️ PythonAnywhere Ready:** Zero-configuration SQLite setup live at `https://juba.pythonanywhere.com`.


---

## 🛠️ Tech Stack

- **Backend:** Python 3 (Flask)
- **Database:** SQLite3 (`products.db`)
- **PDF Engine:** `pdfplumber` + Custom Arabic Bidirectional Normalizer
- **Frontend:** Vanilla HTML5, CSS3 Glassmorphism, Cairo Google Font, JavaScript (Fetch API)
- **Mobile:** Android Native WebView Wrapper (`android-app/`)

---

## 🤖 AI-Assisted Engineering | التطوير بالذكاء الاصطناعي

تم تطوير وتحسين هذا المشروع بالتعاون مع تقنيات الذكاء الاصطناعي التوليدي (**AI-Assisted Pair Programming**)، مما ساهم في تقديم حلول متقدمة تشمل:
- **معالجة النصوص العربية الذكية (Arabic NLP Normalization):** خوارزمية مخصصة لتوحيد جميع أشكال الهمزات والألف (`أ/إ/آ/ا`)، والتاء المربوطة والهاء (`ة/ه`)، والياء والألف المقصورة (`ي/ى`) وإزالة التشكيل، لضمان دقة نتائج البحث بنسبة 100%.
- **استخراج ومعالجة ملفات الـ PDF:** بناء نظام ذكي لمعالجة النصوص العربية المعكوسة تلقائياً واستخلاص الأسعار والأصناف بدقة وسرعة فائقة.
- **تصميم واجهة مستخدم فاخرة (Dark & Gold Glassmorphism):** واجهة عصرية وسلسة متوافقة تماماً مع شاشات الهواتف والكمبيوتر.
- **تطبيق أندرويد متكامل:** بناء التطبيق وتجهيز الأيقونات التكيفية (Adaptive Icons) لجميع أبعاد الشاشات.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/AbnaaEldawy.git
cd AbnaaEldawy
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create your local `.env` file based on `.env.example`:
```bash
cp .env.example .env
```
Default contents:
```env
DB_PATH=products.db
ADMIN_PIN=1234
```

### 4. Run the Application
```bash
python app.py
```
Open your browser at `http://localhost:5000` or `http://127.0.0.1:5000`.

---

## ☁️ Deployment on PythonAnywhere

1. Create a Web App on [PythonAnywhere](https://www.pythonanywhere.com/) (select **Manual configuration** with **Python 3.10+**).
2. Clone or upload the repository files into your PythonAnywhere directory:
   ```bash
   git clone https://github.com/YOUR_USERNAME/AbnaaEldawy.git /home/YOUR_USERNAME/AbnaaEldawy
   ```
3. Install dependencies in the PythonAnywhere console:
   ```bash
   pip3 install -r requirements.txt
   ```
4. In your Web App configuration tab:
   - Set **Source code** to `/home/YOUR_USERNAME/AbnaaEldawy`
   - Set **Working directory** to `/home/YOUR_USERNAME/AbnaaEldawy`
   - Edit the **WSGI configuration file** to point to `app`:
     ```python
     import sys
     path = '/home/YOUR_USERNAME/AbnaaEldawy'
     if path not in sys.path:
         sys.path.append(path)

     from app import app as application
     ```
5. Click **Reload Web App**. Your site will be live at `https://YOUR_USERNAME.pythonanywhere.com`!

---

## 📡 API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Web interface homepage |
| `GET` | `/api/products?search=` | Search products by name (returns all if search is empty) |
| `POST` | `/api/products` | Add a new product (`name`, `selling_price`, `purchase_price`) |
| `PUT` | `/api/products/<id>` | Update an existing product's name or price |
| `DELETE` | `/api/products/<id>` | Delete a product by ID |
| `POST` | `/api/admin/update-pdf` | Bulk update products from uploaded PDF file (`pin`, `pdf`) |

---

## 📁 Project Structure

```text
├── app.py                 # Flask server, API endpoints, PDF parsing logic
├── products.db            # SQLite database
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore configuration
├── templates/
│   └── index.html         # Responsive web application interface
├── static/                # Logo and static image assets
├── android-app/           # Android application project source code
├── AbnaaElDawy.apk        # Built Android installation package
└── README.md              # Documentation
```

---

## 👤 Author

**Mohamed Hossam (Juba)**
- Email: [m.hossam01102078685@gmail.com](mailto:m.hossam01102078685@gmail.com)
- Phone: [+20 1102078685](tel:+201102078685)
- WhatsApp: [Chat on WhatsApp](https://wa.me/qr/CKFJLNTSQSOPI1)

جميع الحقوق محفوظة © 2025 أبناء الضوى للتجارة والتوزيع
