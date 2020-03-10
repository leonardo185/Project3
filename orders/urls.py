from django.urls import path
from orders.views import PostsView

from . import views

urlpatterns = [
    path("", PostsView.as_view(),  name="index"),
    path("cart", views.cart, name="cart"),
    path("credit", views.credit, name="credit"),

]
