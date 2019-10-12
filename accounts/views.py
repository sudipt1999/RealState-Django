from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #check if user with same user name or email exists
            if User.objects.filter(username=username).exists():
                message.error(request, 'Username is already taken')
                return redirect('redirect')
            if User.objects.filter(email=email).exists():
                message.error(request, 'Email is already used')
                return redirect('redirect')

            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            messages.success(request, "You are registered! Kindly login now")
            return redirect('login')
            
        else:
            message.error(request, 'Passwords do not match')
            return redirect('redirect')

        return redirect('register')
    return render(request, 'accounts/register.html')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
            
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')


    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')