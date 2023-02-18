# website views

from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Hello, world. 9729df58 is the polls index.")