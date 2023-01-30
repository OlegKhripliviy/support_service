from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet

from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from users.models import User
from users.serializers import UserRegistrationSerializer, UserSerializer


class UserAPISet(ViewSet):
    @staticmethod
    def list(request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    @staticmethod
    def retrieve(request, id_: int):
        instants = User.objects.get(id=id_)
        serializer = UserSerializer(instants)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    @staticmethod
    def delete(request, id_: int):
        User.objects.get(id=id_).delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        context: dict = {"request": self.request}
        serializer = UserRegistrationSerializer(
            data=request.data, context=context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, id_: int):
        instance = User.objects.get(id=id_)

        context: dict = {"request": self.request}
        serializer = UserSerializer(
            instance, data=request.data, context=context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)
