from celery import shared_task

from django.core.mail import send_mail

import config

from time import sleep

from cv.models import Application


@shared_task
def send_email_task(email, message, field_to_update):
    send_mail('LMS application', message, config.EMAIL_HOST_USER, [email])
    application = Application.objects.filter(email=email).first()
    setattr(application, field_to_update, True)
    application.save()
    return None
