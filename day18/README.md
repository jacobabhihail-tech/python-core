# Expense Tracker - Day 18

## 📅 Day 18: Forms & CRUD Operations

### Overview
In Day 18, we extended the Expense Tracker project to handle **Forms** and **CRUD** operations, allowing users to manage expenses more effectively.

### ✅ Features Implemented

1. **Forms**
   - Added HTML forms to capture expense details (`name` and `amount`).
   - Validated form input using Django request data.

2. **Create**
   - Users can add new expenses through the form.
   - Data is saved to the database using Django ORM (`Expense.objects.create`).

3. **Read**
   - Displayed a list of all expenses dynamically on the homepage.
   - Updated list reflects newly added expenses.

4. **Update**
   - Implemented edit functionality for expenses.
   - Users can update expense name and amount.
   - Fixed common errors like template paths and POST handling.

5. **Debugging & Error Handling**
   - Corrected typos (`ojects` → `objects`) and template errors.
   - Added debug prints to quickly confirm functionality.

### 🛠 Tech Stack
- **Python 3.11**
- **Django 5.2.10**
- **SQLite3** database

### 📂 Project Structure
