from celery import shared_task
from django.core.mail import send_mail



@shared_task
def send_bulk_email(emails,passwords):
    for i,j in zip(emails,passwords):
        file=open("Varency\emailtemplate.html",'r')
        html=file.read()
        message=f' Hi! {i.split("@")[0]} admin has invited you to join your login credentials are id:{i} password is {j} '
        send_mail('Mail from Varency',message,from_email='info@Varency.com',recipient_list=[i])
    return 




