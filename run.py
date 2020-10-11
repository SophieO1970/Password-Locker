# #!/usr/bin/env python3.8
# import pyperclip #for copying and pasting to our clipboard
# from user import User
# from credential import Credential
# import random #import random variables
# import string #import string constants



# def create_user(username,password):
#     '''
#     Function to create a new user
#     '''
#     new_user = User(username,password)
#     return new_user


# def save_new_user(user):
#     '''
#     Function to save user
#     '''
#     user.save_user()
    
# def create_credential(username, social_name, account_name, password):
#     '''
#     Function to create a new user account
#     '''
#     new_credential = Credential(username, social_name, account_name, password)
#     return new_credential

# def save_credentials(credential):
#     '''
#     Function to save a new user account
#     '''
#     Credential.save_credentials(credential)    
    
# def generate_password(self, pass_len=10):

#         password_chars = string.ascii_letters + string.digits + string.punctuation

#         return ''.join(secrets.choice(password_chars) for i in range(int(pass_len)))    
    
# def delete_credentials(self):
        
#         '''
#         delete_credentials method deletes account objects saved in the credential_list.
#         '''
#         Credential.credential_list.remove(self)    
        
# @classmethod
# def find_by_account_name(cls,name):
    
#         '''
#         Method that takes in a name and returns a credential that matches that name.

#         Args:
#             name: account_name to search for
#         Returns :
#             credential of person that matches the account_name.
#         '''

#         for credential in cls.credential_list:
#             if credential.account_name== name:
#                 return credential        
            
            

# @classmethod
# def copy_credentials(cls, social_name):
#         '''
#         Class method that copies a credential's info after the credential's social account name is entered
#         '''
#         found_credential = cls.find_by_social_name(social_name)
#         return pyperclip.copy(found_credential.account_password)
    
# @classmethod
# def display_credentials(cls):
#         '''
#         This method displays saved credentials
#         '''

#         return cls.credential_list



# def main():
#     print("Hello and welcome to your password locker")
#     print("What is your name?")
#     print('\n')
#     user_name= input()
    
#     while true
#     print('\n')
#     print(f"Hello {user_name}! Use these short codes to navigate through")
#     print('\n')
    
#     print('cn - Create a new password locker account')
#     print('lg - Log in into your created account')
#     print('ex - Exit your password locker account')
#     print('\n')
    
    
#     short_code = input().lower()
#     if short_code == 'cn':
#         print('Create your password locker account')
#         print("-"*10)

#         print("Username...")
#         username = input()

#         print("Key in a password of your choice")
#         password = input()

#         save_new_user(create_user(username,password))

#         print ('\n')
#         print(f"Congratulations {username} your account has been created successfully!")

#         print ('\n')
#         print("Log in using the username and password you have created")

#         print("Username...")
#         login_username = input()

#         print("Password...")
#         login_password = input()

#         if username != login_username or password != login_password:
#             print("Incorrect Username or password!")
#             print("Please re-enter your username...")
#             login_username = input()

#             print("Please re- enter your password....")
#             login_password = input()

#         else :
#              print ('\n')
#              print(f'Hello {login_username}. Welcome to your password locker account!')
#              print ('\n')

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
    