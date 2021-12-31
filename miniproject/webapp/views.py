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
        email = data['email']
        bmi = data['bmi']
        smoke = data['smoke']
        if int(age) > 45:
            return JsonResponse("your age is more than what we expected", safe=False)
        if not str(email).__contains__("@"):
            return JsonResponse("your email seems invalid", safe=False)
        new_user = User(first_name=first_name, last_name=last_name, number=number, age=age, email=email, bmi=bmi,
                        smoke=smoke)
        # new_user.first_name = first_name
        # new_user.last_name = last_name
        # new_user.number = number
        # new_user.age = age
        # new_user.email = email
        # new_user.bmi = bmi
        # new_user.smoke = smoke
        new_user.save()
        return JsonResponse("Registered Successfully", safe=False)


class UserList(APIView):
    def get(self, request):
        user1 = User.objects.all()
        serializer = UserSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
