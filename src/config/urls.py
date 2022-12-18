from django.http import HttpResponse
from django.urls import path


def signup(variable):
    return HttpResponse("Hellow")


urlpatterns = [
    path("signup/", signup),
]
