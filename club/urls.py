from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_page),
    path('members', views.members),
    path('sponsors', views.sponsors),
    path('contact', views.contact),
    path('boardroom', views.boardroom)
]