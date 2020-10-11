import pyperclip #for copying and pasting to our clipboard


class User:
    '''
    Create class that generates new instances of users.
    '''
    
    user_list = []
    
    def __init__(self, username, password):
        
        '''
        Method that defines the properties of a user.
        '''
        
        self.username = username
        self.password = password
        
    def save_user(self):
        
        '''
        Method that saves new user instances/object.
        '''
        
        User.users_list.append(self)
        