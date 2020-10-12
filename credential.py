from user import User
import random #import random variable generator
import string  #import string constants
import pyperclip

class Credential:

    '''
    A class that generates new instances of account names and their credential.
    '''
    
    credential_list =[]
    
    
    
    def __init__(self, username, account_name, password):
        '''
        __init__ method that define properties for our objects.
        Args:
            account_name: new user social account name
            username: new user username
            password: new user password
        '''
        # instance variables
        self.username=username
        self.account_name=account_name
        self.password=password
    
    
    def save_credentials(self):

        '''
        save_credentials a method that saves accounts objects into the credential_list
        '''
        Credential.credential_list.append(self) 
        
    def delete_credentials(self):
        
        '''
        delete_credentials method deletes account objects saved in the credential_list.
        '''
        Credential.credential_list.remove(self)
    
    @classmethod
    def check_user(cls,username,password):
        '''
        Method that checks if the name and password entered exist in the users_list.
        '''
        current_user = ''
        for user in User.user_list:
        	if (user.username == username and user.password == password):
        		current_user = user.username
        return current_user


    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            account_name:  account_name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

        return False


    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in a name and returns a credential that matches that name.

        Args:
            name: account_name to search for
        Returns :
            credential of person that matches the account_name.
        '''

        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential
            
            
            
    @classmethod
    def display_credential(cls):
        '''
        This method displays saved credentials
        '''

        return cls.credential_list

