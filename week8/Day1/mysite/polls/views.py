from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def index (request):
    output = " Hello this is my first django website"

    context = {'greeting': output}

    return  render(request, 'homepage.html', {context})

def profile (request):
        names= ['Tom', 'Sacha','Yuval']
        genders = [ 'F', 'M']

        profile = {'name':random.choice(names)}
        'gender': random.choice(genders)
        return  render(request, 'profile.html', {context})
  