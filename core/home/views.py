from django.shortcuts import render
from django.http import HttpResponse
import random 
# Create your views here.

def index(request):
    #print("request",vars(request))
    lucky_number = random.randint(10,99)
    
    #print("lucky_number",lucky_number)--> to print in local terminal here we use in views.py
    vegetables = ['Tomato','Potato','Chilly']
    for vegetable in vegetables:
        print(vegetable)
    context = {"lucky_number": lucky_number,"vegetables":vegetables}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def dynamic_url(request,id,name):
    print(f'This is the value that we got in function -->{id}')
    return render(request, 'dynamic_url.html', context = {"id":id , "name": name })


def project(request):
    lucky_number = random.randint(10,99)
    context = {"lucky_number": lucky_number}
    return render(request,"project/project.html", context)
