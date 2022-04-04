from django.http import HttpResponse
from django.shortcuts import render


def club_page(request):
    return HttpResponse("Welcome")


def members(request):
    return HttpResponse("Hello Dear Member")


def sponsors(request):
    return HttpResponse("Our list of Sponsors and Partners")


def contact(request):
    return HttpResponse("Contact Us")


def boardroom(request):
    return HttpResponse("Notifications")
