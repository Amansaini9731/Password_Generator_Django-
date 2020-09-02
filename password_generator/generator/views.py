from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/home.html")
def password(request):

    charcters=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charcters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('specialcase'):
            charcters.extend('!@#$%^&*()')
    if request.GET.get('number'):
        charcters.extend('123456789')

    length=int(request.GET.get('length'))
    thepassword = ""
    for x in range(length):
        thepassword+=random.choice(charcters)

    return render(request,"generator/password.html",{'password':thepassword})