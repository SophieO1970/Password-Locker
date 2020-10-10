import unittest
from user import User


class TestUser(unittest.TestCase):
    
    '''
    A test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        A set up method to run before each test cases.
        '''
        self.new_user = User('SophieCee','1234!')
        
    
    # def tearDown(self):
    #     '''
    #     The tearDown method that does the clean up after each test case has run.
    #     '''
    #     User.users_list= []
        
    # def test_init(self):
    #     '''
    #     The test_init test case to test if the object is initialized properly
    #     '''
    #     self.assertEqual(self.new_user.username,'SophieCee')  
    #     self.assertEqual(self.new_user.password,'1234!')  
        
    # def test_save_user(self):
    #     '''
    #     The test_save_user to check whether we can save our user objects to our users_list
    #     '''
    #     self.new_user.save_user()
    #     self.assertEqual(len(User.users_list),1)
        
        

if __name__ == '__main__':
    unittest.main()            
        
    
        
        
        
        
    
    

