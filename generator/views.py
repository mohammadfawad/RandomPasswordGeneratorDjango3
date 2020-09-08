from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'username': 'admin', 'password': 'alpha'})


def apple(request):
    return HttpResponse('<a href="https://www.apple.com/mac/">https://www.apple.com/mac/</a>')


def password(request):
    pas = ''
    length = int(request.GET.get('length', 12))
    upper = bool(request.GET.get('uppercase', False))
    numbers = bool(request.GET.get('number', False))
    special = bool(request.GET.get('specialCharacter', False))
    charsLower = list('abcdefghijklmnopqrstuvwxyz')
    if upper:
        charsLower.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if numbers:
        charsLower.extend('0123456789')
    if special:
        charsLower.extend('~!@#$%^&*()_+?:|')
    for x in range(length):
        pas += random.choice(charsLower)
    return render(request, 'generator/password.html', {'password': pas, 'up': upper, 'number': numbers, 'specials': special, 'length': length})


def about(request):
    return render(request, 'generator/about.html')
