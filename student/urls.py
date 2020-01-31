from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

    path('all/', views.sendAll, name="index"),

    path('random/', views.sendRandom, name="index"),
]