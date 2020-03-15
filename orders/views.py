from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Cart

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


def add_to_cart(request, item_id):
    try:
        user_id = int(request.user.id)
        quantity = int(request.POST["quantity"])
        print(item)

    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})
    except Item.DoesNotExist:
        return render(request, "orders/error.html", {"message": "No flight."})

    add_item = Cart()
    add_item.user = user_id
    add_item.item = int(item_id)
    add_item.quantity = quantity
    add_item.save()

    return HttpResponseRedirect(reverse("description", args=(item_id,)))






def register(request):
    return render(request, "orders/register.html")

def login(request):
    return render(request, "orders/login.html")

@login_required
def cart(request):
    return render(request, "orders/cart.html")

def credit(request):
    return render(request, "orders/credit.html")
