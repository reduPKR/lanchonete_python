from core import models

def create(name, size, value):
    try:
        try_create(name, size, value)
    except:
        return None

def try_create(name, size):
    pass