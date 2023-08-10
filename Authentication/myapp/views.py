from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1==pass2:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')
        else:
            return HttpResponse("Please Give the correct confirm password")
        print(uname,email,pass1, pass2)

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pass1 = request.POST.get('pass1')

        myuser = authenticate(request,username=uname, password=pass1)
        if myuser is not None:
            login(request,myuser)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is Incorrect!!!")
    return render(request, 'login.html')