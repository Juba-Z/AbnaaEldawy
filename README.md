# AbnaaEldawy - Product Management System

A lightweight web-based product management application built with Flask and Microsoft SQL Server. Designed for managing product inventory, prices (wholesale and retail), and quick search.

## Features

- Real-time product search by name
- Add, update, and delete products directly from the interface
- Manage wholesale (`Selling_Price`) and retail (`Purchase_Price`) pricing
- Responsive Arabic RTL interface styled for mobile and desktop

## Tech Stack

- **Backend:** Python (Flask)
- **Database:** Microsoft SQL Server (via `pyodbc`)
- **Frontend:** HTML5, CSS3, JavaScript (Bootstrap RTL)

## Prerequisites

- Python 3.8+
- Microsoft SQL Server
- ODBC Driver 18 for SQL Server

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AbnaaEldawy.git
cd AbnaaEldawy
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Database & Environment
1. Import `products_db.sql` in SQL Server Management Studio (SSMS) to initialize the database and sample data.
2. Create your local environment file:
   ```bash
   cp .env.example .env
   ```
3. Update `.env` with your SQL Server credentials:
   ```env
   DB_SERVER=YOUR_SERVER_NAME
   DB_NAME=products_db
   DB_USER=YOUR_USERNAME
   DB_PASSWORD=YOUR_PASSWORD
   ```

### 4. Run the Application
```bash
python app.py
```
Access the application at `http://localhost:5000`.

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/products?search=` | Retrieve products (supports optional search query) |
| `POST` | `/api/products` | Create a new product |
| `PUT` | `/api/products/<id>` | Update an existing product |
| `DELETE` | `/api/products/<id>` | Delete a product |

## Project Structure

```text
├── app.py                 # Application routes and database logic
├── requirements.txt       # Dependencies
├── products_db.sql        # Database schema and seed data
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── templates/
│   └── index.html         # Frontend interface
└── static/                # Static assets (logos, icons)
```

## Author

Mohamed Hossam (Juba)
