from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from webapp.models import User
from django.utils.crypto import get_random_string

def create_token(users):
    token = get_random_string(length=50)
    return token
