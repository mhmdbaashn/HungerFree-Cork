from django.shortcuts import render
from django.http import HttpResponse


def meal(request):
    return HttpResponse("Hello, HungerFree Cork platform is coming soon!") 