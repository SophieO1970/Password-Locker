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
    
def generate_password(self, pass_len=10):

        password_chars = string.ascii_letters + string.digits + string.punctuation

        return ''.join(secrets.choice(password_chars) for i in range(int(pass_len)))    
    
def delete_credentials(self):
        
        '''
        delete_credentials method deletes account objects saved in the credential_list.
        '''
        Credential.credential_list.remove(self)    