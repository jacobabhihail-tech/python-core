import sqlite3

conn = sqlite3.connect("D:\Python Journey\Python training\python-core\day14\python-sql-mini-project\company.db")
cursor = conn.cursor()

print("Connected to database successfully")


# ----read----

cursor.execute(""" 
INSERT INTO employees (name, salary, dept_id)
VALUES (?,?,?)
""",("Rahul", 60000, 1))

conn.commit()
print('\nEmployee Inserted')

#------update-----
cursor.execute("""
UPDATE employees 
SET salary = ?
WHERE name = ?                            
""", (65000, "Rahul"))

conn.commit()
print("\nEmployee updated")

# ---------delete------
cursor.execute( """
DELETE FROM employees
WHERE name = ?
""", ("Rahul",)
)

conn.commit()
print("\n Employee Deleted")


# ---------------- READ AGAIN ----------------
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()

print("\nEmployees after CRUD:")
for emp in employees:
    print(emp)

conn.close()
print("\nDatabase connection closed")
