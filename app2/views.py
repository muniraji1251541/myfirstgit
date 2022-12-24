from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun3(request):
    return HttpResponse('This is third function')

def fun4(request):
    return HttpResponse('This is fourth function')