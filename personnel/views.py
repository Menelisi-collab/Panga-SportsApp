from django.http import HttpResponse
from django.shortcuts import render


def coaches(request):
    return HttpResponse("Coaches..")


def physios(request):
    return HttpResponse("Physios..")


def players(request):
    return HttpResponse("Players..")


def managers(request):
    return HttpResponse("Managers..")


def travel(request):
    return HttpResponse("Travel..")


def catering(request):
    return HttpResponse("Catering..")


def security(request):
    return HttpResponse("Security..")
