from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def family(request):
            families= {
            "families": [
                {
                    "id": 1,
                    "name": "Felidae"
                },
                {
                    "id": 2,
                    "name": "Caninae"
                }
            ]
        }
            return render(request, 'family.html', {'families':families})

def animal(request):
            animales= {
            {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 2,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        }}
            return render(request, 'animal.html', {'animales':animales})
