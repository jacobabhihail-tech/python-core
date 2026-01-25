# 📅 Day 19 – User Authentication (Django)

## 🚀 What We Built
Added full **user authentication** to the Expense Tracker project using Django’s built-in auth system.

---

## ✅ Features Implemented

- 🔐 User Login
- 🆕 User Signup (Registration)
- 🚪 User Logout
- 🛡️ Protected Views using `@login_required`
- 👤 Django Superuser (Admin access)
- 🧾 Expense CRUD works only after login

---

## 🧩 Concepts Covered

- Django Authentication System
- `authenticate()`, `login()`, `logout()`
- `User` model
- Sessions & Middleware
- Access control with `login_required`
- Handling authentication errors
- Secure password handling

---

## 🗂️ Pages Added

- `/login/` – User login
- `/signup/` – User registration
- `/logout/` – Logout
- `/` – Home (protected)

---

## 🛠️ Tech Stack

- Python 3.11
- Django 5.2
- SQLite3
- HTML Templates

---

## ▶️ How to Run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
