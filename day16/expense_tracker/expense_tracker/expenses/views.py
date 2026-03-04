from django.shortcuts import render
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expesne/expense_list.html',{
        'expenses' : expenses
    })


# Create your views here.

