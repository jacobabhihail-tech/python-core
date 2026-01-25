from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        if name and amount:
            Expense.objects.create(name=name, amount=amount)
        return redirect("/")

    expenses = Expense.objects.all()
    return render(request, 'expenses/home.html', {"expenses": expenses})

def delete_expense(request,id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return redirect('home')

def edit_expense(request, id):
    expense = Expense.objects.get(id=id)

    if request.method == 'POST':
        print("POST DATA:", request.POST)

        expense.name = request.POST.get('name')
        expense.amount = request.POST.get('amount')
        expense.save()
        return redirect('home')
    
    return render(request, 'expenses/edit.html', {'expense': expense})

# Create your views here.
