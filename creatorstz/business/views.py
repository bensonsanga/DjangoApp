from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h1>Home Business</h1>')


def about(request):
    return HttpResponse('<h1>business About page</h1>')
