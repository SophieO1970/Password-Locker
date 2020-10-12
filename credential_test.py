import unittest
from credential import Credential
import pyperclip

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

        self.new_credential = Credential('SophieCee','twitter','1234!')    
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        
        '''
        Credential.credential_list = []
        
        
    def test_init(self):

        '''
        test_init test case to test if the object is initialized properly.
        '''

        self.assertEqual(self.new_credential.username, 'SophieCee')
        self.assertEqual(self.new_credential.account_name, 'twitter')
        self.assertEqual(self.new_credential.password, '1234!')
        
        
    def test_save_credentials(self):
        
        '''
        test_save_credentials test to test if the object is saved into
         the credential list.
        '''
        
        self.new_credential.save_credentials()
        test_credential = Credential('SophieCee', 'twitter', '1234!')
        test_credential.save_credentials()
        self.assertEqual(len(Credential.credential_list), 2)
        

    def test_delete_credentials(self):
        
        '''
        test_delete_credential test to test if the object is removed from
        the credential list.
        '''
         
        self.new_credential.save_credentials()
        test_credential = Credential('SophieCee', 'twitter', '1234!') #new credential
        test_credential.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_account_name(self):
        '''
        test to check if we can find a credential by account_name and display information
        '''

        self.new_credential.save_credentials()
        test_credential = Credentials("Joseph","Instagram","123456") # new credential
        test_credential.save_credentials()

        found_credential = Credentials.find_by_account_name("Instagram")

        self.assertEqual(found_credential.account_name,test_credential.account_name)
    
    def test_find_by_account_name(self):
        '''
        Test to check if the find_by_account_name method returns the correct credential.
        '''
        self.new_credential.save_credentials()
        test_credential = Credential('SophieCee', 'twitter', '1234!')
        test_credential.save_credentials()
        credential_found = Credential.find_by_account_name('twitter')
        self.assertEqual(credential_found.account_name,test_credential.account_name)
        
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_contact to check if we can save multiple
        objects to our credential_list
        '''    

        self.new_credential.save_credentials()
        test_credential =  Credential('SophieCee', 'twitter',  '1234!')
        test_credential.save_credentials()

        self.assertEqual(len(Credential.credential_list),2) 
        
        
    def test_credential_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the credential.
            '''

            self.new_credential.save_credentials()
            test_credential = Credential("SophieCee","twitter","1234!") # new credential
            test_credential.save_credentials()

            credential_exists = Credential.credential_exist("twitter")

            self.assertTrue(credential_exists)    
            

    # def test_copy_account_name(self):
    #     '''
    #     Function to test to if the copying account method copies the correct credential.
    #     '''
        
    #     self.new_credential.save_credentials()
    #     Credential.find_by_account_name("twitter")

    #     self.assertEqual(self.new_credential.account_name,pyperclip.paste())
        
    def test_display_credentials(self):
        '''
        test method that returns a list of all accounts added
        '''
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
        
        

if __name__ == '__main__':
    unittest.main()
    