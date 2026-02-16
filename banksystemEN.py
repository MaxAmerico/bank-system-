user_dict = {'brun0trt': 3023}

print('You have entered the banking system')

signin_or_signup = input('Do you wish to Sign In or Sign Up? (Please type "SI" or "SU"): ').upper()

if signin_or_signup == 'SI': 
    username = input('What is your username? ')
    
    if username in user_dict:
        password = int(input('What is your password? '))
        
        if user_dict[username] == password:
            print('Access granted!')
        else:
            print('Wrong password!')
    else:
        print('User not found.')