from django.http import HttpResponse
from django.shortcuts import render
from . models import Entities


def index(request):
    options = Entities.objects.all()
    context = {'items': options}
    return render(request, 'index.html', context)