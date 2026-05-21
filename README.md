# 🛒 SQLAlchemy Shop Database Project

> A beginner-friendly Python + SQLAlchemy project demonstrating how to build and manage a relational database using ORM models, relationships, CRUD operations, and SQLite.

---

## 📌 Project Overview

This project creates a simple shop database system using:

- 🐍 Python
- 🗄️ SQLite
- ⚡ SQLAlchemy ORM

The application demonstrates:

✅ Creating database models  
✅ One-to-many relationships  
✅ Foreign keys  
✅ CRUD operations  
✅ Relationship navigation  
✅ Cascade deletes  
✅ SQLAlchemy 2.0 typed ORM syntax

---

# 📂 Project Structure

```bash
shop_project/
│
├── shop_v2.py          # Main application script
├── shop_v2.db          # SQLite database file (generated automatically)
└── README.md           # Project documentation
```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| ⚡ SQLAlchemy | ORM framework |
| 🗄️ SQLite | Lightweight local database |
| 🔗 SQLAlchemy Relationships | Table connections |

---

# 🧠 Database Design

The project contains 3 relational tables:

## 👤 Users Table

Stores customer information.

| Column | Type |
|---|---|
| user_id | Integer (PK) |
| username | String |
| email | String |

---

## 📦 Products Table

Stores product inventory.

| Column | Type |
|---|---|
| product_id | Integer (PK) |
| productname | String |
| price | Integer |

---

## 🧾 Orders Table

Links users to purchased products.

| Column | Type |
|---|---|
| order_id | Integer (PK) |
| user_id | Foreign Key |
| product_id | Foreign Key |
| quantity | Integer |

---

# 🔗 Relationship Structure

```text
User
 └── One-to-Many ──► Orders

Product
 └── One-to-Many ──► Orders

Orders
 └── Many-to-One ──► User
 └── Many-to-One ──► Product
```

---

# 🚀 Features

## ✅ Database Initialization

```python
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
```

Recreates the database structure every time the script runs.

---

## ✅ Insert Sample Data

The project automatically creates:

- 👤 Users
- 📦 Products
- 🧾 Orders

Example:

```python
user_a = User(name="Jane Doe", email="jdoe@example.com")
```

---

## ✅ ORM Relationships

Example relationship setup:

```python
orders: Mapped[List["Order"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan"
)
```

This allows automatic object linking between tables.

---

## ✅ Retrieve Records

Examples include:

- All users
- All products
- All orders with linked names

```python
orders = session.scalars(select(Order)).all()
```

---

## ✅ Update Records

Example:

```python
blanket.price = 25
session.commit()
```

Updates product pricing dynamically.

---

## ✅ Delete Records

```python
session.delete(user_to_delete)
session.commit()
```

Cascade delete ensures related orders are removed automatically.

---

# 🧱 SQLAlchemy Concepts Demonstrated

| Concept | Example |
|---|---|
| ORM Models | `class User(Base)` |
| Typed ORM | `Mapped[str]` |
| Foreign Keys | `ForeignKey()` |
| Relationships | `relationship()` |
| Session Management | `session.commit()` |
| CRUD Operations | Create, Read, Update, Delete |
| Cascade Delete | `delete-orphan` |

---

# ▶️ How To Run

## 1️⃣ Install SQLAlchemy

```bash
pip install sqlalchemy
```

---

## 2️⃣ Run The Script

```bash
python shop_v2.py
```

---

# 🖥️ Example Console Output

```text
SQLite engine configured!
Database structure recreated successfully!
Successfully added users, products, and split Diana's orders!

--- 1. RETRIEVING ALL USERS ---
User ID: 1 | Username: Jane Doe | Email: jdoe@example.com

--- 2. RETRIEVING ALL PRODUCTS ---
Product Name: Snuggle Blanket | Price: $10

--- 3. RETRIEVING ALL ORDERS WITH NAMES ---
Order ID: 1 | Buyer: Jane Doe | Item: Snuggle Blanket | Qty: 1

--- 4. UPDATING A PRODUCT'S PRICE ---
Old Price for Snuggle Blanket: $10
New Price for Snuggle Blanket: $25 updated successfully!

--- 5. DELETING A USER BY ID ---
User ID 1 has been deleted!
```

---

# 📖 Learning Goals

This project is excellent practice for learning:

- 🧠 SQLAlchemy ORM fundamentals
- 🗄️ Relational database design
- 🔗 Table relationships
- ⚡ CRUD workflows
- 🐍 Python database programming
- 🧱 Object-oriented database modeling

---

# 🔮 Possible Future Improvements

Ideas for expanding the project:

- 🛍️ Shopping cart system
- 💳 Checkout/payment handling
- 📊 Inventory tracking
- 🔍 Product search
- 🌐 Flask or FastAPI web interface
- 👥 User authentication
- 📈 Admin dashboard
- 📱 Mobile-friendly frontend

---

# 📚 Resources

- 📘 SQLAlchemy Documentation  
  https://www.sqlalchemy.org/

- 🐍 Python Documentation  
  https://docs.python.org/3/

- 🗄️ SQLite Documentation  
  https://www.sqlite.org/docs.html

---

# 👩‍💻 Author

Built as a SQLAlchemy ORM learning project using Python and SQLite.

---

# ⭐ License

This project is open-source and free to use for educational purposes.
