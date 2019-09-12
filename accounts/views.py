from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':

        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password_again = request.POST['password_again']


            # Input check.
            input = {
                "first_name" : first_name,
                "last_name" : last_name,
                "username" : username,
                "email" : email,
                "password" : password,
                "password_again" : password_again,

            }

            if input["password"] == input["password_again"]:
                if User.objects.filter(username = username):
                    print("Username is taken.")
                elif User.objects.filter(email = email):
                    print("email  is taken")
                else:
                    user = User.objects.create_user(username = input["username"], password = input["password"], email = input["email"], first_name = input["first_name"], last_name = input["last_name"])
                    user.save()
                    print(f"user created")
                    return redirect('/')
            else:
                return redirect('/')
        except KeyError:
            return render(request, "accounts/register.html", {"message": "Incomplete Credentials"})

    else:
        return render(request, "accounts/register.html")
