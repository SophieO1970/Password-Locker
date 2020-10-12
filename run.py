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


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

    
def create_credential(username, account_name, password):
    '''
    Function to create a new user account
    '''
    new_credential = Credential(username, account_name, password)
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
             
    
def generate_password(length = 10):
    '''
    Function that generates password automatically
    '''
    letters = string.ascii_lowercase
    password_generated = ''.join(random.choice(letters) for i in range(length))
    return password_generated

   
def verify_user(username,password):
    '''
    Function that veryfies the existing user
    
    '''
    check_user = Credential.check_user(username,password)
    return check_user


def check_existing_account(account_name):
    '''
    Function that checks if ctredential exists
    '''
    return Credential.find_by_account_name(account_name)


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
    print(' ')
    print('Hello! Welcome to password Locker')
    while True:
        print("--"*50)
        print('\n')
        
        print('Use these short codes to navigate through: \n ca - Create an Account \n lg - Login \n ex - Exit')
        print('\n')
        short_code = input().lower().strip()
        if short_code == 'ex':
            break 
        
        elif short_code == 'ca':
            print("-"*20)
            print('\n')
            print('Create a new account:')
            print('\n')
           
            username = input('Enter your User name - ')
            password = input('Enter your password - ')
            save_user(create_user(username, password))
            # print(" ")
            print(f'New Account Created for: {username} using password: {password}')
            print('\n')

        elif short_code == 'lg':
            print("--"*50)
            print('\n')
            print('Enter your account details to login:')
            print('\n')
            username = input('Enter your username - ')
            password = str(input('Enter your password - '))
            user_exists = verify_user(username,password)
            if user_exists == username:
                print('\n')
                print(f'Welcome {username}. Please select a short code to continue.')
                print(' ')

                while True:
                    print("--"*50)
                    print('Our short codes: \n cc-Create a Credential \n sc-Show Credentials \n fc- Find a Credential  \n ex-Exit')
                    print('\n')
                    short_code = input('Enter a choice: ').lower()
                    print("-"*10)


                    if short_code == 'ex':
                        print(" ")
                        print(f'Thank you for using Password Locker. Goodbye {username}')
                        # break

                    elif short_code == 'cc':
                        print('\n')
                        print('Enter your new credentials:')
                        print('\n')  
                        
                        account_name = input('Enter your account name - ')

                        while True:
                            print('\n')
                            print("-"*20)
                            print('Please select an option for creating a password: \n ep - enter your password \n gp - generate a password \n ex - exit')
                            choice = input('Enter an option: ').lower()
                            print("-"*10)
                            
                            if choice == 'ep':
                                
                                print('\n')
                                password = input('Enter your password: ')
                                break
                            elif choice == 'gp':
                                password = generate_password()
                                break
                            elif choice == 'ex':
                                break
                            else:
                                print('Wrong option entered. Try again!')

                        save_credential(create_credential(username,account_name,password))
                        print('\n')
                        print(f'Credential Created: Account Name: {account_name} - Password: {password}')
                        print('\n')    
                    elif short_code == 'fc':
                        print("Enter the account name you want to search for:")
    
                        account_name = input()
                        if check_existing_account(account_name):
                                credential = find_credential(account_name)
                                print(f"Here is the Credentials for {credential.account_name} ")
                                print('\n')
                                print(f'account Name: {credential.account_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                                print('\n')
                                print('-' * 20)
        
                        else:
                                print('\n')
                                print("That credential does not exist")
                                
                                
                    elif short_code == 'rc':
                        print('\n')
                        print("Enter the account name of the credentials you want to remove")
                        print('\n')
    
                        account_name = input('Enter the account name- ')
                        # del_credential(credential)

                        if find_credential(account_name):
                                credential = find_credential(account_name)
                                credential.delete_credentials()									
                                print("Here is a list of all deleted credentials")
                                print('\n')


                        else:
                                print('\n')
                                print("That credential does not exist")
                                print('\n')

                    elif short_code == 'sc':
                        print('\n')
                        if display_credential(username):
                            print('Here is a list of all your credentials')
                            print("  ")
                            for credential in display_credential(username):
                                print(f'account Name: {credential.account_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print('\n')
                        else:
                            print('\n')
                            print("You don't seem to have saved any credentials yet. enter cc to create one.")
                            print('\n')

                    elif short_code == 'copy':
                        print(' ')
                        account_name = input('Enter the account name for the credential password to copy: ')
                        copy_credentials(account_name)
                        print('\n')
                    else:
                        print('Wrong option entered. Try again!')

            else:
                print(' ')
                print('Wrong details entered. Try again or Create an Account!')

        else:
            print("-"*20)
            print('\n')
            print('Wrong option entered. Try again!')    

if __name__ == '__main__':
	main()