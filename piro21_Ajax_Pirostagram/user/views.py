from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout 
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
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

def user_search(req):
    query = req.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
    else:
        users = User.objects.none()
    return render(req, 'user_search.html', {'users': users})

