from django.shortcuts import render,redirect 
from django.http import HttpResponse
import random 
from home.forms import ContactForm
import requests
from home.models import Contact, Product 
from django.contrib import messages 
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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save() #once the form is validated it will be saved
            return redirect('/contact/')
    
    form = ContactForm()
    context = {'form': form}
    return render(request,"contact.html",context)

def dynamic_url(request,id,name):
    print(f'This is the value that we got in function -->{id}')
    return render(request, 'dynamic_url.html', context = {"id":id , "name": name })


def project(request):
    lucky_number = random.randint(10,99)
    context = {"lucky_number": lucky_number}
    return render(request,"project/project.html", context)

def request_product(request):
    
    if request.method == "POST":
        print(request.POST)
        product_name = request.POST.get('product_name')
        quantity = request.POST.get('quantity')
        remarks = request.POST.get('remarks')
        file = request.FILES['file']

        product = Product.objects.create(
            product_name = product_name,
            quantity = quantity,
            remarks = remarks ,
            file = file
        )
        messages.success(request,"Profile created.")
        return redirect('/request-product/')
    return render(request,'request.html')
