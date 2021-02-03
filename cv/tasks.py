from celery import shared_task

from django.core.mail import send_mail

import config

from time import sleep


@shared_task
def send_email_task():
    sleep(5)
    send_mail('Email Sent with celery', 'Proof', config.EMAIL_HOST_USER, [config.EMAIL_HOST_USER])
    return None
