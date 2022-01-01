from django.utils.crypto import get_random_string


def create_token(users):
    token = get_random_string(length=50)
    return token
