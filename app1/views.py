from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse('This is first function')

def fun2(request):
    return HttpResponse('This is second function')