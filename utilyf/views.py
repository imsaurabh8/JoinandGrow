from django.shortcuts import render
from django.shortcuts import HttpResponse,render

# Create your views here.
def index(request):
    return render(request,'utilyf/index.html')

def about(request):
    return render(request,'utilyf/about.html')