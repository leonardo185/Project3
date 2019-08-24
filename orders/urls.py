from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("cart", views.cart, name="cart"),
    path("credit", views.credit, name="credit"),

]
