import string
from random import *
from user import User
from user import Credentials



def create_user(first_name,last_name,user_name,user_password):
    new_user = User (first_name,last_name,user_name,user_password)
    return new_user


def save_user(user):
    user.save_user()


def  delete_user(User):
    user.delete_user()

def find_user(number):
    return User.find_by_number(number)

def display_users():
    return User.display_users()

def create_accout(account_user_name,account_name,account_password):
    new_account= Credentials(account_user_name,account_name,account_password)
    return new_account

def save_account(user):
    user.save_account()

def delete_account(user):
    user.delete_account()

def find_account(number):
    return Credentials.find_by_number(number)


def display_accounts():
    return Credentials.display_accounts()


def main():

    while True:
        print("Welcome to password Locker! choose  one of the options to begin")
        print("SignUp -or- LogIn")
        option=input()
        
        if option == "SignUp":
            print("create account")
            print("-"*10)
            print("Enter First Name ..")
            first_name=input()

            print("Enter Last Name..")
            last_name=input()

            print("Set your Username ..")
            user_name=input()

            print("Set your password")
            user_password=input()

            # create_user(first_name,last_name,user_name,user_password)

            # save_user();
            

            print("Thank you for registering an account with us.Here are your details:")
            print("-"*10)
            print(f"Name: {first_name} {last_name} \nUsername: {user_name} \nPassword: {user_password}")
            print("\nNow you can LogIn using these details")
            print("\n \n")
        
        elif option == "LogIn":
            print("Enter Username .. ")
            login_user_name=input()

            print("enter your password ..")
            login_password=input()

            if find_user(login_password):
                print("\n")
                print("Welcome! Choose any option from the ones provided below:")
                print("-"*60)

                print("Add_account -or-View_accounts")

                choose=input()
                print("\n")

                if choose=="Add_account":
                    print("Add Credentials account")
                    print("-"*25)
                    account_user_name=login_user_name
                    print("Account Name")
                    account_name=input()

                    print("\n")
                    print("Generate automatic password(generate  or Create your own personal password(create)?")
                    decision=input()

                    if decision =="generate":
                        characters=string.ascii_letters +string.digits
                        account_password="".join(choice(characters) for x in range(randint(8,16)))
                        print(f"password:{account_password}")
                        
                    elif decision =="create":
                        print("Enter your password")
                        account_password=input()
                    
                    else:
                        print("Invalid choice,try again")
                    save_account(create_account(account_user_name,account_name,account_password))
                    print("\n")
                    print(f"Username:{account_user_name} \nAccount Name:{account_name} \nPassword:{account_password}")


                elif choose == "ViewAccounts":
                    if find_account(account_user_name):
                        print("List of all your accounts: ")
                        print("-"*25)

                        for user in display_accounts():
                            print(f"Account:{user.account_name} \Password:{user.account_password} \n\n")
                        
                        else:
                         print("invalid credentials")
                    
                else:
                    print("Incorrect username or password,please try again")
                    print("\n")
            else:
                print("Incorrect option,choose from the one's listed")
                print("\n")

if __name__ == '__main__':
     
     
     main()
                     

                


                        
