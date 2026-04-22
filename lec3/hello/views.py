from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
    # rendering html files instead of hardcode it here allows us to seperate python files and html files

def hugh(request):
    return HttpResponse("Hello, Hugh!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize() # Here we pass all the information to that specific html file using a dictionary
    })

