from django.shortcuts import render
from apple_people.models import People
# Create your views here.

def index(request):
    ceos = People.objects.all()
    return render(request, "people.html", context ={"ceos": ceos })
