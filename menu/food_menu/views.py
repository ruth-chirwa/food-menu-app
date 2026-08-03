from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the Food Menu App!")


def item(request):
    return HttpResponse("This is the item view.")