#!/usr/bin/env python3.8
import pyperclip #for copying and pasting to our clipboard
from user import User
from credential import Credential
import random #import random variables
import string #import string constants

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

def save_credential(credential):
    '''
    Function to save a new user account.
    '''
    Credential.save_credentials(credential)   
      
def delete_credential(self):
        
        '''
        delete_credential method deletes account objects saved in the credential_list.
        '''
        Credential.credential_list.remove(self)    
             
    
def generate_password(self, pass_len=10):

        password_chars = string.ascii_letters + string.digits + string.punctuation

        return ''.join(secrets.choice(password_chars) for i in range(int(pass_len)))    
   
def verify_user(user_name,password):
    '''
    Function that veryfies the existing user
    
    '''
    check_user = Credential.check_user(user_name,password)
    return check_user


def find_credential(account_name):
    '''
    Function that credential by account_name and returns credential.
    '''
    return Credential.find_by_account_name(account_name)
            
# def copy_credential(credential):
#     '''
#     Function that displays saved credentials
#     '''
#     return Credential.display_credential()

def display_credential(credential):
    '''
    Function that displays saved credentials
    '''
    return Credential.display_credential()



def main():
    print("Hello and welcome to your password locker")
    print("What is your name?")
    print('\n')
      user_name= input()

    while true
    print('\n')
    print(f"Hello {user_name}! Use these short codes to navigate through")
    print('\n')
    
    print('cn - Create a new password locker account')
    print('lg - Log in into your created account')
    print('ex - Exit your password locker account')
    print('\n')
    
    
    short_code = input().lower()
    if short_code == 'cn':
        print('Create your new password locker account')
        print("-"*30)


        user_name = input('Enter your User name - ')
        password = input('Enter your password - ')
        save_user(create_user(user_name, password))

        print(f"Congratulations {username} your account has been created successfully using password : {password}")
        print ('\n')
        
        print ('\n')
        print("Log in using the username and password you have created")

        print("Username...")
        login_username = input()

        print("Password...")
        login_password = input()

        if username != login_username or password != login_password:
            print("Incorrect Username or password!")
            print("Please re-enter your username...")
            login_username = input()

            print("Please re- enter your password....")
            login_password = input()

        else :
             print ('\n')
             print(f'Hello {login_username}. Welcome to your password locker account!')
             print ('\n')

#     elif short_code == 'lg':
             
#             print('Log in to your existing account')
#             print('Username....')
#             lg_username = input()

#             print('Password....')
#             lg_password = input()

#             if lg_username != 'SophieCee' and lg_password != '1234!':
#                 print('The account does not exist, please create an account')
#             else:
#                 print(f'Hello {lg_username}. Welcome to your password locker account!')
#                 print ('\n')
#     elif short_code == 'ex':

#             print('Bye! Pass by again later!')
#             break
#     else:
#             print('Error!Unknown short code! Please try again')
    