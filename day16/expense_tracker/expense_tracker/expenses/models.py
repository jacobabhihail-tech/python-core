from django.db import models

# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()
    description = models.TextField(blank= True, null= True)

    def __str__(self):
        return f"{self.title} - {self.amount}"