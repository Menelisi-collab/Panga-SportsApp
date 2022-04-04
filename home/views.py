from django.http import HttpResponse
from django.shortcuts import render
from . models import Entities


def index(request):
    options = Entities.objects.all()
    return render('index.html', {'items': options})
    return HttpResponse('Welcome To PANGA',)