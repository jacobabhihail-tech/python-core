# Day 16 – Django Models, Migrations & ORM

## What was done
- Created a new Django project and app
- Defined a database model using Django Models
- Applied migrations to create database tables
- Used Django ORM to perform CRUD operations

---

## Expense Model

```python
from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"


python manage.py makemigrations
python manage.py migrate


python manage.py shell


from expenses.models import Expense

# Create
Expense.objects.create(title="Tea", amount=20, date="2026-01-16")

# Read
Expense.objects.all()

# Get single object
expense = Expense.objects.get(id=1)

# Update
expense.amount = 25
expense.save()

# Delete
expense.delete()
