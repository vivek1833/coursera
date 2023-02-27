# website views

from django.shortcuts import HttpResponse

def owner(request):
        return HttpResponse("Hello, world. ba077326 is the polls owner.")