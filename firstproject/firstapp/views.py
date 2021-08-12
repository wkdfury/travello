from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Man


def demo(request):
    obj=Place.objects.all()
    obj1=Man.objects.all()
    return render(request,"index.html",{'result':obj,'ans':obj1})
# def addi(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     ans=x+y
#     sub=x-y
#     mult=x*y
#     div=x/y
#     return render(request,'result.html',{'result':ans,'subst':sub,'multi':mult,'divi':div})

# def hello(request):
#     return render(request,"result.html")

# Create your views here.
