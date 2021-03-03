from django.shortcuts import render
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator_practice/home.html')

def generator(request):
    password = ''
    password_chars = string.ascii_lowercase

    for _ in range(int(request.GET.get('length'))):
        if request.GET.get('uppercase'):
            password_chars = string.ascii_letters
        if request.GET.get('numbers'):
            password_chars += string.digits
        if request.GET.get('special'):
            password_chars += string.punctuation
        password += random.choice(password_chars)

    return render(request, 'generator_practice/generator.html', {'x':password})
