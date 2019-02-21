from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Benson',
        'title': 'Post 1',
        'content': 'My first test post in django',
        'date_posted': 'February 21 2019'
    },
    {
        'author': 'Bosco',
        'title': 'IDK',
        'content': 'Hey there',
        'date_posted': 'February 25 2019'
    },
    {
        'author': 'Benjamin',
        'title': 'ENGINES',
        'content': 'I am an engineer',
        'date_posted': 'February 11 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'community/home.html', context)


def about(request):
    return render(request, 'community/about.html', {'title': 'About'})
