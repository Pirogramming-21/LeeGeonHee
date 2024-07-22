from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout 
from django.urls import reverse
# Create your views here.
def signup(req):
    if req.method == 'GET':
        signupForm = UserCreationForm()
        ctx = {
            'signupForm': signupForm
        }
        return render(req, 'user/signup.html', ctx)
    elif req.method == 'POST':
        signupForm = UserCreationForm(req.POST)
        if signupForm.is_valid():
            user = signupForm.save()
            user.save()
        return redirect('/user/login') 
    
def login(req):
    if req.method == 'GET':
        loginForm = AuthenticationForm()
        ctx = {
            'loginForm': loginForm
        }
        return render(req, 'user/login.html', ctx)
    elif req.method == 'POST':
        loginForm = AuthenticationForm(req, req.POST)
        if loginForm.is_valid():
            auth_login(req, loginForm.get_user())
            return redirect(reverse('board:board_list')) 
        else:
            ctx = {
                'loginForm': loginForm
            }
            return render(req, 'user/login.html', ctx)
def logout(req):
    auth_logout(req)
    return redirect('/user/login' )
