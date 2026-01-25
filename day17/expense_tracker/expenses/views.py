from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        if name and amount:
            Expense.ojects.create(name=name, amount=amount)
        return redirect("/")

    expenses = Expense.objects.all()
    return render(request, 'expenses/home.html', {"expenses": expenses})

# Create your views here.
