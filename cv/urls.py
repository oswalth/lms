from django.urls import path, include
from .views import ApplicationView, index

urlpatterns = [
    path('', ApplicationView.as_view(), name='application'),
    path('task/', index, name='task')
]

