from .models import *

def get_material():
    materials = Task.objects.all()
    return materials