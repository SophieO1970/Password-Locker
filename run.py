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


def save_new_user(user):
    '''
    Function to save user
    '''
    user.save_user()
    
def create_credential(username, social_name, account_name, password):
    '''
    Function to create a new user account
    '''
    new_credential = Credential(username, social_name, account_name, password)
    return new_credential
def save_credentials(credential):
    '''
    Function to save a new user account
    '''
    Credential.save_credentials(credential)    