from django.http import HttpResponse;
from django.shortcuts import render;


def home(req):
    # return HttpResponse("Hello World, I am Muhammad Arslan")

    return render(req,"index.html")

def about(req):
    return HttpResponse("Hello World, I am Muhammad Arslan on about us page")

def contact(req):
    return HttpResponse("Hello World, I am Muhammad Arslan on <h1>Contact Us </h1>")
