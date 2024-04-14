from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "About.html")

def service(request):
    return render(request, "Service.html")

def product(request):
    return render(request, "Product.html")

def contact(request):
    return render(request, "Contact.html")

def signuppage(request):
    return render(request, "Signup.html")

def loginpage(request):
    return render(request, "Login.html")