from django.urls import path
from . import views


urlpatterns = [
    path('', views.scheduling),
    path('notifications', views.notifications)
]


