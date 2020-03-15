from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegistrationForm, DealerRegisterForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



# Create your views here.

# User Registration.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form' : form})

#Dealer Registration.
def dealer_register(request):
    if request.method == 'POST':
        form = DealerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            company = form.cleaned_data.get('company_name')
            messages.success(request, f'Dealer account created for {company}! We will get in touch with you soon.')
            return redirect('index')
    else:
        form = DealerRegisterForm()
    return render(request, 'accounts/dealer_register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def load_items(request):
    data = {
        'items': Item.objects.all()
    }
    return JsonResponse(data)
