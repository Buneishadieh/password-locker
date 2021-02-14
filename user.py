import random
import string
class User:
    """
    class that generates new instances of users
    """
    users_list=[]

    def _init_(self,first_name,last_name,user_name,password):
        """
        _init_method that helps us define properties of our objectsself.
        Args:
        first_name:New user first_name
        last_name:New  user last_name
        user_name:New  user user_name
        password:New user password
        """
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.password=password
    

    def save_user(self):
        """
        save_user method user objects into user userslist
        """
        User.users_list.append(self)
    

    def delete_user(self):
        """
        delete_user method deletes a saved user from the users_list
        """
        User.users_list.remove(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the users_list
        """
        return cls.users_list 

    @classmethod
    def find_by_number(cls,number):
        """
        method that takes in  username and returns  a user that matches that number
        Args:
        number:phone numbner to search for Returns :Contact of person that matches the number.
        """
        for user in cls.users_list:
            if user.password==number:
                return User

    @classmethod
    def user_exist(cls,number):
        for user in cls.users_list:
            if user.user_name==number:
                return True
                return False


class  Credentials:
    """
    class that generates new instances of credentials
    """
    accounts=[]
    def _init_(self,account_user_name,account_name,account_password):
        """
        _init_method that helps us define [roperties  for objectsself.
        Args:
        account_user_name:new credentials account_user_name
        account_name:new credentials account_name
        account_password:new credentials account_password
        """
        self.account_user_name=account_user_name
        self.account_name=account_name
        self.account_password=account_password
    def save_account(self):
         """
        save_account method saves user objects into  accounts
        """
         Credentials.accounts.append(self)
       
    
    def delete_account(self):
        """
        delete_account method deletes a saved Credential from accounts
        """
        Credentials.accounts.remove(self)



    @classmethod
    def display_accounts(cls):
        """
        method that returns the accounts
        """
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls,number):
        """
        method that takes and returns a contact that matches that number

        Args:
        number:account_user_name to search for Returns :credentilas of user that matches the number.
        """
        for account in cls.accounts:
            if account.account_user_name==number:
                return account           
    
