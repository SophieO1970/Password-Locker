import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviour.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    
    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''

        self.new_credential = Credential('SophieCee', 'twitter','SophieO','1234!')    
    
#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run.
        
#         '''
#         Credential.credential_list = []
        
        
#     def test_init(self):

#         '''
#         test_init test case to test if the object is initialized properly.
#         '''

#         self.assertEqual(self.new_credential.username, 'SophieCee')
#         self.assertEqual(self.new_credential.social_name, 'twitter')
#         self.assertEqual(self.new_credential.account_name, 'SophieO')
#         self.assertEqual(self.new_credential.password, '1234!')
        
        
#     def test_save_credentials(self):
        
#         '''
#         test_save_credentials test to test if the object is saved into
#          the credential list.
#         '''
        
#         self.new_credential.save_credentials()
#         test_credential = Credential('SophieCee', 'twitter', 'SophieO', '1234!')
#         test_credential.save_credentials()
#         self.assertEqual(len(Credential.credential_list), 2)
        

#     def test_delete_credentials(self):
        
#         '''
#         test_delete_credential test to test if the object is removed from
#          the credential list.
#          '''
         
#         self.new_credential.save_credentials()
#         test_credential = Credential('SophieCee', 'twitter', 'SophieO', '1234!') #new credential
#         test_credential.save_credentials()
#         self.new_credential.delete_credentials()
#         self.assertEqual(len(Credential.credential_list), 1)

#     def test_find_by_account_name(self):
#         '''
#         Test to check if the find_by_account_name method returns the correct credential.
#         '''
#         self.new_credential.save_credentials()
#         test_credential = Credential('SophieCee', 'twitter', 'SophieO', '1234!')
#         test_credential.save_credentials()
#         credential_found = Credential.find_by_account_name('SophieO')
#         self.assertEqual(credential_found.SophieO,test_credential.SophieO)
        
#     def test_save_multiple_credentials(self):
#         '''
#         test_save_multiple_contact to check if we can save multiple
#         objects to our credential_list
#         '''    

#         self.new_credential.save_credentials()
#         test_credential =  Credential('SophieCee', 'twitter', 'SophieO', '1234!')
#         test_credential.save_credentials()

#         self.assertEqual(len(Credential.credential_list),2) 
            

#     def test_copy_credentials(self):
#         '''
#         Function to test to if the copy credential method copies the correct credential.
#         '''
#         self.new_credential.save_credentials()
#         test_credential = Credential('SophieCee', 'twitter', 'SophieO', '1234!')
#         test_credential.save_credentials()
#         found_credential = None
#         for credential in Credential.credential_list:
#             found_credential = Credential.find_by_social_name(
#                 credential.social_name)
            
#             return pyperclip.copy(found_credential.password)
#         Credential.copy_credentials(self.new_credential.site_name)
#         self.assertEqual('1234!', pyperclip.paste())
#         print(pyperclip.paste())
        
#     def test_display_credentials(self):
#         '''
#         test method that returns a list of all accounts added
#         '''
#         self.assertEqual(Credential.display_credentials(),Credential.credential_list)
        
        

# if __name__ == '__main__':
#     unittest.main()
    