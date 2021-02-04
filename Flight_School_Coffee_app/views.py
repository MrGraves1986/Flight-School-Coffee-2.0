from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request,'index.html')

def contact_us(request):
    return render(request, 'contact.html')

def about_us(request):
     return render(request, 'about.html')

