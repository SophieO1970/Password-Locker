


class User:
    '''
    create class that allows user to generate user account
    '''
    
    user list = []
    
    def __init__(self,user_name,password):
        
        '''
        Method that defines the properties of a user.
        '''
        
        self.user_name = user_name
        self.password = password
        
#     def save_user(self):
        
#         '''
#         Method that saves new user instances.
#         '''
        
#         User.user_list.append(self)
        