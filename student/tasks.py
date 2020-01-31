
from celery import shared_task
from time import sleep

from django.core.mail import send_mail

from .models import StudentProfile
from django.shortcuts import render, redirect,HttpResponse
from django.conf import settings
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@shared_task
def send_mail_task():
    print("zilani")
    ak = StudentProfile.objects.all()
    # print(ak)
    mail_list = []
    for v in ak:
        mail_list.append(v.email)
    print(mail_list)

    send_mail("celery task check!",'This proved the Task worked properly','humyaira2019@gmail.com',mail_list)
    return None


@shared_task
def single_send_mail_task():

    send_mail("celery task check!",'This proved the Task worked properly','humyaira2019@gmail.com',['sadmanshihab111@gmail.com'])
    return None



@periodic_task(
    run_every=(crontab(minute='*/25')),
    name="send_mail",
    ignore_result=True
)

@shared_task
def sleepy(duration):
    sleep(duration)
    return None
