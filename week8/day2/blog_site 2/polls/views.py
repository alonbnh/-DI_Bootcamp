from django.shortcuts import render
from django.http import HttpResponse
import random 

person = {
    'Name': 'Yossi',
    'GitHub': 'yussieik@github.com',
    'Address': 'Tel Aviv'
}

def index(request):

    output = "Hello this is my first website!"

    context = {'greeting': output, **person}

    return render(request, 'homepage.html', context)

def profile(request):

    names = ['Tom','Sasha','Yuval']
    genders = ['F', 'M']

    profile = {'name':random.choice(names), 
    'gender': random.choice(genders)}

    return render(request, 'profile.html', profile)