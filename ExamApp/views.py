from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from LogRegApp.models import User
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'AllQuotes': Quote.objects.all(),
        'User': User.objects.get(id=request.session['log_user'])
    }
    return render(request, 'quotes.html', context)

def create_quote(request):
    if request.method == 'POST':
        errors = Quote.objects.QuoteValidator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/quotes')
        user= User.objects.get(id=request.session['log_user'])
        newAuthor = request.POST['author']
        newQuote = request.POST['quote_desc']
        Quote.objects.create(quote_user=user, quote_desc=newQuote, author=newAuthor)
    return redirect('/quotes')

def user(request, UserId):
    context ={
        'AllQuotes': Quote.objects.filter(quote_user=UserId),
        'User': User.objects.get(id=UserId)
    }
    return render(request, 'user.html', context)

def myaccount(request, UserId):
    context = {
        'User': User.objects.get(id=UserId)
    }
    return render(request, 'account.html', context)

def edit(request):
    if request.method == 'POST':
        ToUpdate = User.objects.get(id=request.session['log_user'])
        ToUpdate.first_name = request.POST['first_name']
        ToUpdate.last_name = request.POST['last_name']
        ToUpdate.email = request.POST['email']
        ToUpdate.save()
        return redirect('/quotes')
    return redirect('/')

def delete(request, QuoteId):
    toDelete = Quote.objects.get(id=QuoteId)
    toDelete.delete()
    return redirect('/quotes')

def logout(request):
    request.session.flush()
    return redirect('/') 

def back(request):
    return redirect('/quotes')


