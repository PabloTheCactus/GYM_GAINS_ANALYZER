from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "authentication/index.html")

def signin(request):
    return render(request, "authentication/signup.html")

def signup(request):
    return render(request, "authentication/signup.html")

def signout(request):
    pass