from django.urls import path
from . import views


urlpatterns = [
    path('', views.coaches),
    path('physios', views.physios),
    path('players', views.players),
    path('managers', views.managers),
    path('travel', views.travel),
    path('catering', views.catering),
    path('security', views.security)
]