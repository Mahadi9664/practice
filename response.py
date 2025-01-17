from validator_collection import validators, checkers, errors

email = input("What's your email address: ")

try:
    email_address = validators.email(email)
    if(email_address):
       print("Valid")
    else:
        print("Invalid")
    
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")