from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'expenses/login.html', {
                'error':'Invalid username or password'
            })
        
    return render(request, 'expenses/login.html')

@login_required(login_url='/login/')
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        if name.strip() and amount:
            Expense.objects.create(name=name.strip(), amount=float(amount))
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

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            return render(request, 'expenses/signup.html', {
                'error' : 'Password do not match'
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, "expenses/signup.html", {
                'error' : 'Username already exists'
            })
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request,user)
        return redirect('home')
    
    return render(request, 'expenses/signup.html')