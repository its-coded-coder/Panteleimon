from django.shortcuts import render,redirect
from django.http import HttpRequest
# Create your views here.

def index(request):
    return render(request,'index.html')

def activities(request):
    # if request.method=='post':
        return render(request,'edu.html')

def root_redirect(request):
    return redirect('/')