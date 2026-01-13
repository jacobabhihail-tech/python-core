# Day 12 – SQL Basics (CRUD Operations)

This repository contains my **Day 12 learning** as part of my journey to become a **Python AI Engineer**.

The focus of this day was understanding **SQL fundamentals** and performing **CRUD operations**, which are essential for handling real-world data used in AI and machine learning projects.

---

## Why SQL Matters for Python AI Engineers

Most AI systems follow this flow:

Database (SQL) → Python (Pandas / NumPy) → Machine Learning Model

SQL is used to:
- Store structured data
- Filter and clean datasets
- Prepare data before model training

---

## Tools Used

- Database: SQLite  
- GUI Tool: DB Browser for SQLite  
- OS: Windows  

---

## Database Information

- Database Name: `company.db`
- Table Name: `employees`

### Table Structure
- id (INTEGER, Primary Key)
- name (TEXT)
- department (TEXT)
- salary (INTEGER)

---

## SQL Operations Performed

### CREATE TABLE
```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
);
