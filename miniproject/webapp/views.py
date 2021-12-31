import json
from . import db
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
        password = data['password']
        password2 = data['password2']
        username = data['username']

        if db.username_is_in_db(username):
            return JsonResponse("This username has been taken before", safe=False)
        if not password2 == password:
            return JsonResponse("your passwords does not match", safe=False)
        new_user = User(first_name=first_name, last_name=last_name, number=number, password=password, username=username)
        db.add_to_db(new_user)
        return JsonResponse("Registered Successfully", safe=False)


class Login(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        q1 = User.objects.filter(username__startswith=username)
        for users in q1:
            if users.password == password:
                return JsonResponse("Logged in Successfully", safe=False)
        return JsonResponse("password doesnt match", safe=False)


class Insurance(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        age = data['age']
        email = data['email']
        bmi = data['bmi']
        smoke = data['smoke']
        token = data['token']
        if int(age) > 45:
            return JsonResponse("your age is more than what we expected", safe=False)
        if not str(email).__contains__("@"):
            return JsonResponse("your email seems invalid", safe=False)
        new_insurance_user = User(age=age, email=email, bmi=bmi, smoke=smoke)
        db.add_to_db(new_insurance_user)
        return JsonResponse("Registered Successfully", safe=False)


class UserList(APIView):
    def get(self, request):
        user1 = User.objects.all()
        serializer = UserSerializer(user1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
