from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home/')
        else:
            return(request, 'login.html', {'error' : 'invalid credentials'})
        
def user_signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST ['username']
        password = request.POST ['password']
        user = User(username = username)
        user.set_password(password)
        user.save()
        return redirect('login')
    
def logout_view(request):
    logout(request)  
    return redirect('login') 


def home_page(request):
    return render(request, 'home.html')