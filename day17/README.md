# Expense Tracker - Day 17

## Overview
This Django project allows users to track their expenses. On Day 17, we focused on setting up the project, creating the app, models, and displaying expenses.

## Features Completed
- **Project Setup**: Created Django project `expense_tracker`
- **App Creation**: Created `expenses` app and registered it in `INSTALLED_APPS`
- **Model**: `Expense` model with fields:
  - `title` (string)
  - `amount` (decimal)
  - `description` (optional text)
  - `created_at` (auto timestamp)
- **Database**: Applied migrations, database `db.sqlite3` created
- **Views**: Display all expenses
- **URLs**: Configured project and app URLs
- **Templates**: Created template to render expenses
- **Server**: Ran Django development server successfully
- **Outcome**: Can view all expenses; shows "No expenses yet!" if database is empty

## Next Steps
- Day 18: Add Forms and CRUD operations (Create, Read, Update, Delete)

## How to Run
1. Clone the repository
2. Install dependencies: `pip install django`
3. Run server: `python manage.py runserver`
4. Open browser at `http://127.0.0.1:8000/`
