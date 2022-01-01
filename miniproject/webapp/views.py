import hashlib
import json

from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated

from . import db, middleware
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
        password = make_password(password, salt=None, hasher='default')
        new_user = User(first_name=first_name, last_name=last_name, number=number, password=password,
                        username=username, has_insurance='False', smoke='False')
        db.add_to_db(new_user)
        return JsonResponse("Registered Successfully", safe=False)


class Login(APIView):

    def post(self, request, format=None):
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        q1 = User.objects.filter(username__startswith=username)
        for users in q1:
            if users.username == username:
                if check_password(password, users.password):
                    token = middleware.create_token(users)
                    User.objects.filter(username=username).update(token=token)
                    return JsonResponse({"result": "Logged in Successfully", "token": token}, safe=False)
        return JsonResponse("password doesnt match", safe=False)


class Insurance(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        age = data['age']
        email = data['email']
        bmi = data['bmi']
        smoke = data['smoke']
        token = data['token']
        q1 = User.objects.filter(token__startswith=token)
        if len(q1) == 0 or token == "0" or token == "":
            return JsonResponse("You're Not authorized", safe=False)
        if age == "" or email == "" or bmi == "" or smoke == "":
            return JsonResponse("please enter all needed information", safe=False)
        if int(age) > 45:
            return JsonResponse("your age is more than what we expected", safe=False)
        if not str(email).__contains__("@"):
            return JsonResponse("your email seems invalid", safe=False)
        User.objects.filter(token=token).update(age=age, email=email, bmi=bmi, smoke=smoke, has_insurance='True')
        return JsonResponse("You Are Successfully Registered In Our Insurance", safe=False)


class Logout(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        token = data['token']
        User.objects.filter(token=token).update(token="")
        return JsonResponse("Logged out Successfully", safe=False)
