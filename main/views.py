from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    d={}
    return render(request,'main/index.html')