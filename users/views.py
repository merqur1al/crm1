from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group

from store.models import *
from .forms import AuthUserForm
from .decorators import unauthenticated_user

@unauthenticated_user
def registerPage(request):
    form = AuthUserForm()
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('users:login')

    context = {'form':form}
    return render(request, 'users/registerPage.html', context)

@unauthenticated_user
def loginPage(request):
    form = AuthUserForm()
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('/')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {'form':form}
    return render(request, 'users/loginPage.html', context)


def logoutPage(request):
    logout(request)

    return redirect('users:login')

