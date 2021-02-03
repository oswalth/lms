from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .forms import ApplicationForm

from .tasks import send_email_task


def index(request):
    send_email_task.delay()
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
            # application = form.save(commit=False)
            # application.image = request.FILES.get('image')
            # application.save()
            form.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')