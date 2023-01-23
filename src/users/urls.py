from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import path
from rest_framework.generics import CreateAPIView, ListAPIView

from users.serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()


class UserCreateAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UsersGet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_ticket(request, id_: int) -> JsonResponse:
    user: User = User.objects.get(id=id_)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


urlpatterns = [
    path("", UserCreateAPI.as_view()),
    path("list/", UsersGet.as_view()),
]
