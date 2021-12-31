from .models import User


def username_is_in_db(username):
    users = User.objects.all()
    for user in users:
        if user.username == username:
            return False
    return True


def add_to_db(user):
    user.save()
