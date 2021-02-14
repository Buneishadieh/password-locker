import unittest
from user import user
from user import credentials

class test_user(unittest.TestCase):
    """
    Test class that defines test cases for the User Class behaviours
    """
    def set_Up(self):
        """
        Set up method to run before each test cases
        """
        self.new_user=user("bunei","Shadrack","buneishadieh","1@Shadrack")

    def tear_down(self):
        """
        tear-down method that does clean up after each test case has been return
        """
        user.users_list=[]

    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name,"Shadrack")
        self.assertEqual(self.new_user.last_name,"bunei")
        self.assertEqual(self.new_user.user_name,"buneishadieh")
        self.assertEqual(self.new_user.password,"1@Shadrack")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the userslist
        """
        self.new_user.save_user()
        self.assertEqual(len(user.users_list),1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to test if we can save multiple user to our userslist
        """
        self.new_user.save_user()
        test_user= User("TestFirst","TestLast","TestUsername","TestPassword")
        test_user.save_user()
        self.assertEqual(len(user.users_list),2)


    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user list
        """
        self.new_user.save_user()
        test_user= user("Anne","Mwangi","072319213","annemwangi@gmail.com")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(user.userslist),1)


    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(user.display_users(),User.userslist)


    def test_find_user_by_number(self):
        """
        test to check if we can find a user by their password and display the user
        """

        self.new_user.save_user()
        test_user=user("test_first","test_last","test_user_name","test_password")
        test_user.save_user()

        found_user = User.find_by_number("test_password")
        self.assertEqual(found_user.password,test_user.password)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the contact
        """
        self.new_user.save_user()
        test_user=user("test_first","test_last","test_user_name","test_password")
        test_user.save_user()

        user_exists= user.user_exist("test_user_name")
        self.assertTrue(user_exists)




class test_credentials(unittest.TestCase):
    def set_up(self):
        """
        Test class that defines test cases for the Credentials Class behaviours
        """
        self.new_account = credentials("buneishadieh","Instagram","1@Shadrack")

    def tear_down(self):
        """
        tearDown method that does clean up after each test case has been return
        """
        credentials.accounts=[]

    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.new_account.account_user_name,"buneishadieh")
        self.assertEqual(self.new_account.account_name,"Instagram")
        self.assertEqual(self.new_account.account_password,"1@Shadrack")


    def test_save_account(self):
        """
        test_save_account test case to test if the credentials object is saved into accounts
        """
        self.new_account.save_account()
        self.assertEqual(len(credentials.accounts),1)

    def test_save_multiple_accounts(self):
        """
        test_save_multiple_accounts to test if we can save multiple credentials to accounts
        """
        self.newa_ccount.save_account()
        test_account=credentials("test_user_name","test_account","password")
        test_account.save_account()
        self.assertEqual(len(credentials.accounts),2)

    def test_delete_account(self):
        """
        test_delete_account to test if we can remove a credential from our account
        """
        self.new_account.save_account()
        test_account=credentials("buneishadieh","Twitter","1@Shadrack")
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(credentials.accounts),1)

    def test_display_all_accounts(self):
        """
        method that returns a list of all credentials saved
        """
        self.assertEqual(credentials.display_accounts(),credentials.accounts)

    def test_find_user_by_number(self):
        """
        test to check if we can find a credential by their accountusername and display the credential
        """
        self.newaccount.save_account()
        test_account=credentials("test_user_name","test_account","Password")
        test_account.save_account()

        found_account = credentials.find_by_number("test_user_name")
        self.assertEqual(found_account.account_user_name,test_account.account_user_name)


if __name__ == '__main__':
    (unittest.main())