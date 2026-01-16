# 📅 Day 15 – Django Basics (Project Setup)

## 🎯 Objective
Set up the Django development environment and successfully run the first Django project.  
This day focuses on **foundation**, structure, and understanding how Django works before building features.

---

## 🛠️ Tech Stack
- Python 3
- Django 5.2.10
- Visual Studio Code
- Windows PowerShell / VS Code Terminal

---

## 📁 Project Structure
day15/
│
├── manage.py
└── expense_tracker/
├── init.py
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py


---

## 🧠 Key Concepts Learned

### Django Project
- Represents the entire web application
- Contains global settings and configurations

### manage.py
- Command-line utility for:
  - Running the server
  - Managing apps
  - Database migrations

---

## 🚀 Steps Completed

1. Installed Django using pip
   ```bash
   pip install django

   django-admin --version

   django-admin startproject expense_tracker .

   python manage.py runserver

   http://127.0.0.1:8000/
   




