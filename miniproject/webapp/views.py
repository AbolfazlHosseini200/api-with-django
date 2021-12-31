import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


# Create your views here.
class Register(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        first_name = data['first_name']
        last_name = data['last_name']
        number = data['number']
        age = data['age']
        print(first_name, last_name)
        print("test")
        return JsonResponse(first_name, safe=False)


class UserList(APIView):
    def get(self, request):
        user1 = User.objects.all()
        serializer = UserSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
