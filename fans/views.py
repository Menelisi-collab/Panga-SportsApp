from django.http import HttpResponse
from django.shortcuts import render


def merchandise(request):
    return HttpResponse("Purchase Club Merchandise here")
