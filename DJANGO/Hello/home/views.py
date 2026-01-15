from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth import authenticate ,login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    context={
        'variable1':"this is sent",
        'variable2':"Raj is great"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")
    
def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')
def contact(request):
    if request.method == "POST":
        print(request.POST)

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc', '').strip() 

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
            date=datetime.today()
        )
    return render(request, 'contact.html')

def shop(request):
    return render(request, "shop.html")
def tshirts(request):
    return render(request, "tshirts.html")
def tracks(request):
    return render(request, "tracks.html")
def jeans(request):
    return render(request, "jeans.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        # Username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        # Email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "register.html")

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not User.objects.filter(email=email).exists():
            return render(request, "forgot_password.html", {
                "error": "Email not found"
            })

        return render(request, "forgot_password.html", {
            "success": "Password reset link will be sent to your email"
        })

    return render(request, "forgot_password.html")

