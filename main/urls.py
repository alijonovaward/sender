from django.urls import path
from .views import send_form

urlpatterns = [
    path('', send_form, name='send_form'),
]
