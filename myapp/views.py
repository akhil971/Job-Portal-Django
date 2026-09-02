from django.shortcuts import render, redirect
from .models import client_msg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

# Create a new client_msg object and save it to the database
        client_message = client_msg.objects.create(
            name=name, 
            email=email, 
            phone=phone, 
            message=message
            )

        return redirect('/')  # Redirect to the home page after saving the message
    return render(request, 'contact.html') 

# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def companies(request):
    return render(request,'companies.html')
def Job_detail(request):
    return render(request,'Job_detail.html')
def jobs(request):
    return render(request,'jobs.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Log the user in
            return redirect('/')  # Redirect to the home page after successful login
        else:
            # Handle invalid login credentials
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create a new client_msg object and save it to the database
        User.objects.create_user(username=name, email=email, password=password)

        return redirect('/')  # Redirect to the home page after saving the message
    return render(request,'register.html')


def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')  # Redirect to the home page after logout