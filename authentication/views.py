from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home (request):
    return render(request,"authentication/index.html")
def signup (request):

    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        myuser = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password = password1)
        myuser.save()
 
        messages.success(request, "Your Acccount has been created successfully")
        return redirect('signin')
    return render(request, "authentication/signup.html")

def signin (request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')



    return render(request, "authentication/signin.html")
    
def signout (request):
   pass
