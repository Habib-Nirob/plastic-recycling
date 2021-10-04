from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import models

# Create your views here.
def home(request):
    return render(request, 'home.html')

def Blogs(request):
    return render(request,'Blogs.html')
    

def Contact(request):
    if request.method=="POST":
        
        email = request.POST['email']
        message = request.POST['message']
        # print(email, message)
        contact = Contact(email=email,message=message)
        contact.save()
        print("written to the db")
    return render(request,'contact.html')

def offset(request):
    return HttpResponse("this is home page")

def forbands(request):
    return HttpResponse("this is home page")

def signup(request):
    return HttpResponse("this is home page")