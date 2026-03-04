from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()

    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    context = {
        'expenses' : expenses,
        'form': form
    }
    return render(request, 'expenses/expense_list.html', context)
