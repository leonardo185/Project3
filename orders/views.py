from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView


class PostsView(ListView):
    model = Item
    paginate_by = 6
    context_object_name = 'items'
    template_name = 'orders/index.html'
    ordering = ['title']


def register(request):
    return render(request, "orders/register.html")

def login(request):
    return render(request, "orders/login.html")

@login_required
def cart(request):
    return render(request, "orders/cart.html")

def credit(request):
    return render(request, "orders/credit.html")
