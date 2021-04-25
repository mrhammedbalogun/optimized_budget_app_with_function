from datetime import datetime
import random

users_database = {}

def login():
    username = input("\n\nPlease input your username below: \n\n>").lower()
    if username == users_database["username"]:
        password = input("\n\nPlease input your password: \n\n>").lower()
        if password == users_database["password"]:
            menu()
        else:
            print("\n\nLooks like you entered a wrong password\n\n")
    else:
        print("\n\nLogin not correct\n\n")


def register():
    username = input("\n\nPlease enter preferred username: \n\n>").lower()
    if username in users_database:
        print("\n\nLooks like you're already register. Kindly login below\n\n")
        login()

    else:
        first_name = input("\n\nPlease enter first name: \n\n>")
        last_name = input("\n\nPlease enter last name: \n\n>")
        email = input("\n\nPlease enter your email: \n\n>")
        password = input("\n\nPlease input your preferred password: \n\n>").lower()
        account_no = random.randrange(1111111111,9999999999)


        users_database["account_no"] = account_no
        users_database["username"] = username
        users_database["first_name"] = first_name
        users_database["last_name"] = last_name
        users_database["email"] = email
        users_database["password"] = password
        users_database["account_balance"] = 0

        print(f"\n\nCongrat, your account as been successfully created. Your account number is {account_no}. Kindly login below with your username: '{username}': ")

        login()
        fullname = first_name + " " + last_name

    return fullname

def quit_option():
    your_option = input("\nKindly select an option below. Enter MM or LO\n\n [mm] To go back to Menu\n [lo] To log out\n\n\n>").lower()
    if your_option == "mm":
        menu()
    elif your_option == "lo":
        quit()


def user_profile():
    print("Welcome to user profile page\n")
    print(f"\nAccount number: {users_database['account_no']}\nUsername: {users_database['username']}\nFirst Name: {users_database['first_name']}\nLast Name: {users_database['last_name']}\nEmail: {users_database['email']}\nPassword: {users_database['password']}\nAccount Balance: {users_database['account_balance']}\n")
    quit_option()


def deposit():
    deposit_amt = int(input("\n\nPlease input the amount you want to deposit: \n\n>"))
    balance = users_database["account_balance"]
    balance += deposit_amt
    users_database["account_balance"] = balance

    print(f"\n\nYou have successfully deposited NGN{deposit_amt}, your total account balance is now NGN{balance}.\n")

    quit_option()



    

def withdraw():
    withdraw_amt = int(input("\n\nPlease input the amount you want to withdraw: \n\n>"))
    balance = users_database["account_balance"]
    balance -= withdraw_amt
    users_database["account_balance"] = balance

    print(f"\n\nYou have successfully withdrew NGN{withdraw_amt}, your left account balance is now NGN{balance}.\n")

    quit_option()


def check_balance():
    balance = users_database["account_balance"]
    print(f"\n\nYour account balance is NGN{balance}\n")

    quit_option()
    

def complaint():
    print("\n\nWelcome to our complaint section. Kindly give us a call or send us an email.\n\n\nEmail: ouremail@ourcompany.com\n\nPhone number: +2348023900964")
    
    quit_option()



def menu():
    print(f"\n\nWelcome {users_database['first_name']} to menu items\n")
    select_data = input("\nKindly select an option below. Enter AC, DP, WT, CO or UP\n\n [ac] To check account balance\n [dp] To make deposit\n [wt] To withdraw\n [co] To make complaint\n [up] To view your profile\n\n>").lower()
    if select_data == "ac":
        check_balance()
    elif select_data == "dp":
        deposit()
    elif select_data == "wt":
        withdraw()
    elif select_data == "co":
        complaint()
    elif select_data == "up":
        user_profile()
    else:
        print("Invalid selection")



def start_menu():

        
    while True:
        select_data = input("\nKindly select an option below. Enter RG or LG\n\n [lg] To Login\n [rg] To Register\n\n\n>").lower()
                                
        if select_data == 'lg':
            login()

            
        elif select_data == 'rg':
            register()


def init():
    start_menu()       

init()


"""
if __name__ == "__main__":
	main()"""