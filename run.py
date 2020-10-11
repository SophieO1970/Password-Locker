#!/usr/bin/env python3.8
from user import user
from credential import Credential
import random
import string



def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user