# Expense Tracker - Day 21

📅 **Day 21: Refactor, Clean UI, Update README**

## Overview

This is the final version of the **Expense Tracker** app after Day 21.  
In this step, we focused on:

1. **Refactoring**:
   - Improved code readability in `views.py`.
   - Added comments and removed redundant code.
   - Made `edit` and `home` views cleaner.

2. **Clean UI**:
   - Updated HTML templates (`home.html`, `edit.html`, `login.html`, `signup.html`) for better styling.
   - Added **Bootstrap 5** to make the app look professional.
   - Made forms and tables more user-friendly.

3. **Output**:
   - A fully functional Expense Tracker web app with authentication.
   - Users can **login, signup, add, edit, delete expenses**.
   - Responsive, clean design with Bootstrap.

---

## Features

- **User Authentication**:
  - Login
  - Logout
  - Signup

- **Expense Management**:
  - Add expense (name + amount)
  - Edit expense
  - Delete expense
  - View all expenses in a table

- **Clean UI**:
  - Bootstrap forms and tables
  - Styled buttons for actions
  - Responsive layout

- **Admin Panel**:
  - View expenses in Django admin
  - Manage users
  - Permissions handled via Django admin

---

## Technologies Used

- Python 3.11
- Django 5.2
- SQLite (default Django DB)
- HTML / CSS
- Bootstrap 5 (via CDN)

---

## How to Run

1. Clone the repository:
```bash
git clone <your-repo-url>
cd expense_tracker
