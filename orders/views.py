from django.http import HttpResponse, Http404
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

def item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    context = {
        "item": item
    }

    return render(request, "orders/item.html", context)



def register(request):
    return render(request, "orders/register.html")

def login(request):
    return render(request, "orders/login.html")

@login_required
def cart(request):
    return render(request, "orders/cart.html")

def credit(request):
    return render(request, "orders/credit.html")
