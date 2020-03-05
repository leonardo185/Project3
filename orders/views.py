from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def register(request):
    return render(request, "orders/register.html")

def login(request):
    return render(request, "orders/login.html")

@login_required
def cart(request):
    return render(request, "orders/cart.html")

def credit(request):
    return render(request, "orders/credit.html")
