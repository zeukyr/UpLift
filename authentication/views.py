from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists.")
            return redirect("signup")
        
        if password != confirm_password:
            messages.error(request, "Passwords don't match.")
            return redirect("signup")
        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect("signin")

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, "authentication/index.html")
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, "authentication/signin.html")

def Signout(request):
    logout(request)
    return redirect("home")

def Forums(request):
    return render(request, "authentication/Forums.html")

def about(request):
    return render(request, "authentication/about.html")

def feedback(request):
    return render(request, "authentication/feedback.html")

def riceu(request):
    return render(request, "authentication/riceu.html")

def kingscollege(request):
    return render(request, "authentication/kingscollege.html")

def uofsydney(request):
    return render(request, "authentication/uofsydney.html")