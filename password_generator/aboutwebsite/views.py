from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    Characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        Characters.extend(list('0123456789'))
    
    lenght = int (request.GET.get('lenght', 10))
    
    thepassword = ''
    for x in range (lenght):
        thepassword += random.choice(Characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})

def aboutwebsite(request):
    return render(request, 'aboutwebsite/aboutwebsite.html')
