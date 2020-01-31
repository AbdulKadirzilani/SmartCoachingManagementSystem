#from rest_framework import generics
from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import ListView
from .models import StudentProfile
from .tasks import sleepy,send_mail_task,single_send_mail_task
from django.conf import settings
from django.core.mail import send_mail


class HomeView(ListView):
    #template_name = "home.html"
    model = StudentProfile

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('StudentProfile')



def sendAll(request):
    #message will going start after 10 second running code
    #sleepy(10)
    #@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
    
    send_mail_task()
    return HttpResponse("<h1>All mail sent Task is success </h1>")


def sendRandom(request):
    #message will going start after 10 second running code
    #sleepy(10)
    single_send_mail_task()
    return HttpResponse("<h1>Using celery Random mail send is success </h1>")


