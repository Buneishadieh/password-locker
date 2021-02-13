import string
fron random import *
from user import user
from user import credentials


def create_user(first_name,last_name,user_name,user_password):
    new_user = user(first_name,last_name,user_name,user_password)
    return new_user