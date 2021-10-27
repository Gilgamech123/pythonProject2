from .models import *


def get_material(user_id):
    materials = Task.objects.filter(User_id=user_id)
    return materials


def autoriz(login, password):
    users = User.objects.filter(user_login=login, user_password=password)
    return users
