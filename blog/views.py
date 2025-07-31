from django.shortcuts import render

def home(req):
    return render(req,"blog.html")

# Create your views here.

