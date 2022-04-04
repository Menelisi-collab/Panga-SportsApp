from django.http import HttpResponse
from django.shortcuts import render


def scheduling(request):
    return HttpResponse("Find Schedules here")


def notifications(request):
    return HttpResponse("Notifications below")
