from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(auto_now_add= True)

    def __str__(self):
        return f"self.name - ₹{self.amount}"

# Create your models here.
