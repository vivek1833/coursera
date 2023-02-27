# website views

from django.shortcuts import HttpResponse

def home(request):
        return HttpResponse("Hello, world. 9729df58 is the polls index.")

def owner(request):
        return HttpResponse("Hello, world. ba077326 is the polls index.")