import re

"""
Write a function that uses regular expressions to make sure the 
password string it is passed is strong. A strong password is defined 
as one that is at least eight characters long, contains both uppercase 
and lowercase characters, and has at least one digit. 
You may need to test the string against multiple regex patterns
 to validate its strength.
"""
def enterPW():
    check = 0
    while check == 0:
        pw = input("What is your password?")
        if pwStrength(pw) == True:
            check = 1

def pwStrength(password):
    pwLower = re.compile(r'[a-z]')
    pwUpper = re.compile(r'[A-Z]')
    pwNumber = re.compile(r'[0-9]')

    mo1 = pwLower.search(password)
    mo2 = pwUpper.search(password)
    mo3 = pwNumber.search(password)

    if len(password)<8:
        print("Your password needs to be at least 8 characters")
        return False
    elif mo1 == None:
        print("Your password needs at least one lowercase letter")
        return False
    elif mo2 == None:
        print("Your password needs at least one uppercase letter")
        return False
    elif mo3 == None:
        print("Your password needs at least one numeric character")
        return False
    else:
        print("Your password meets the requirements!")
        return True
            


#main
enterPW()


