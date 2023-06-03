from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.RegValidator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        hashedPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
        email=request.POST['email'], password=hashedPW)
        request.session['log_user'] = User.objects.last().id
        return redirect('/quotes')
    return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = User.objects.LoginValidator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        request.session['log_user'] = User.objects.get(email=request.POST['log_email']).id
        return redirect('/quotes')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')