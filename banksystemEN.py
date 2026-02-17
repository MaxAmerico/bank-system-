import random
import time


users_dict = {'brun0trt': 'headxyz2'}

print('Welcome to the Banking System')


auth_choice = input('Do you want to sign in or sign up? (Type SI to Sign In or SU to Sign Up): ').upper()

if auth_choice == 'SI': 
    username = input('Enter your username: ')
    
    if username in users_dict:
        password = input('Enter your password: ')
        
        if users_dict[username] == password:
            print(f'Hello, {username}!')
            print('Balance: $0')
            # I used the Random library to create the system that generates a random account number
            account_number = random.randint(1, 9999)
            print(f'Account Number: {account_number}')
            
            print('What would you like to do?')
            # Note: These variables store the input if you decide to add logic later
            withdraw_money = input('1. Withdraw money: ')
            donate_money = input('2. Donate money: ')
            deposit_money = input('3. Deposit money: ')
            show_transactions = input('4. Show transactions: ')

        else:
            print('Incorrect password!')
    else:
        print('User not found.')

else:
    #Here I am trying to made a while system, it is very hard to do it
    is_running = True
    while is_running:
        print('Please, create your username and password.')
        new_username = input('Enter your username: ')
        new_password = input('Enter your password: ')
        
        if new_username in users_dict:
            print('Sorry, this username already exists.')
            # Added a break or logic change here would prevent an infinite loop
            break 
        else:
            if new_password.isdigit():
                print('Your password must contain at least 5 letters and 1 number.')
                break
            else:
                print('Accessing the system...')
                break
