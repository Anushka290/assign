from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def  home(request):
    #return HttpResponse('Hey')
     return render(request,'demo/home.html')
def table(request):
    return render(request,'demo/table.html')     