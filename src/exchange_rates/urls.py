from api import convert
from django.urls import path

urlpatterns = [
    path("convert/", convert),
]
