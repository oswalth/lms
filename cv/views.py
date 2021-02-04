from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.html import escape
from django.views.generic import View

from datetime import datetime, timedelta
from .forms import ApplicationForm
from .models import Application

from .tasks import send_email_task


def index(request):
    send_email_task.apply_async(('oswalth3@gmail.com', "CV is accepted"), countdown=1)
    return HttpResponse('<h1>Email has been sent with celery!</h1>')


class ApplicationView(View):

    def get(self, request, *args, **kwargs):
        form = ApplicationForm()
        context = {
            'form': form
        }
        return render(request, 'application.html', context)

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            snippet = form.cleaned_data.get('snippet')
            if application := Application.objects.filter(email=email).first():
                application.delete()
            form.save()

            application = form.save(commit=False)
            # application.snippet = escape(snippet)
            send_email_task.apply_async((email, "CV is accepted", "first_email"), countdown=0)
            send_email_task.apply_async((email, "CV is being processed", "second_email"),
                                        eta=datetime.utcnow() + timedelta(days=1))
            application.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
