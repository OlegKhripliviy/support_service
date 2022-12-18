from django.urls import path
from django.http import HttpResponse


def signup(variable):
    return HttpResponse("Hellow")


urlpatterns = [
    path("signup/", signup),
]
