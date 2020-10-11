class Credential:

    '''
    A class that generates new instances of account names and their credential.
    '''
    
    credential_list =[]
    
    
    
    def __init__(self, username, social_name, account_name, password):
        '''
        __init__ method that define properties for our objects.
        Args:
            account_name: new user social account name
            username: new user username
            password: new user password
        '''
        # instance variables
        self.username=username
        self.social_name=social_name
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
        
    def generate_password(self, pass_len=10):

        password_chars = string.ascii_letters + string.digits + string.punctuation

        return ''.join(secrets.choice(password_chars) for i in range(int(pass_len)))
    # def
    
    @classmethod
    def find_by_account_name(cls,name):
        '''
        Method that takes in a name and returns a credential that matches that name.

        Args:
            name: account_name to search for
        Returns :
            credential of person that matches the account_name.
        '''

        for credential in cls.credential_list:
            if credential.account_name== name:
                return credential

    @classmethod
    def copy_credentials(cls, social_name):
        '''
        Class method that copies a credential's info after the credential's social account name is entered
        '''
        found_credential = cls.find_by_social_name(social_name)
        return pyperclip.copy(found_credential.account_password)
    
    @classmethod
    def display_credentials(cls):
        '''
        This method displays saved credentials
        '''

        return cls.credential_list

