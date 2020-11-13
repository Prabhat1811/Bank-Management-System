'''
checks the input 
'''
import check


def username():
    while True:
        username = input('NAME : ')
        if check.username(username):
            return username
        else:
            print('\n**INVALID CUSTOMER NAME**\n')


def email():
    while True:
        email = input('EMAIL ID : ')
        if check.email_id(email):
            return email
        else:
            print('\n**INVALID EMAIL ID**\n')


def phone_number():
    while True:
        phone_number = input('PHONE NUMBER : ')
        if check.phone_number(phone_number):
            return phone_number
        else:
            print('\n**INVALID PHONE NUMBER**\n')


def amount():
    while True:
        amount = input('AMOUNT : ')

        try:
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print('\n**AMOUNT SHOULD BE GREATER THAN 0**\n')
        except:
            print('\n**INVALID AMOUNT**\n')


def account_type():
    while True:
        try:
            acc_type = input('TYPE(CURRENT/SAVINGS) : ').lower()
            if acc_type == 'current' or acc_type == 'savings':
                return acc_type
            else:
                print('\n**INVALID ACCOUNT TYPE**\n')
        except:
            print('\n**INVALID ACCOUNT TYPE**\n')


def password():
    print('\nPASSWORD SHOULD BE 8 OR LONGER MUST CONTAIN ATLEAST 1 DIGIT 1 UPPERCASE ALPHABET 1 LOWERCASE ALPHABET\n')
    while True:
        password = input('PASSWORD : ')
        if check.password(password):
            return password
        else:
            print('\n**INVALID PASSWORD**\n')


def card_pin():
    print('\nPIN SHOULD BE OF 4 DIGITS\n')
    while True:
        pin = input('PIN : ')
        if check.pin(pin):
            return pin
        else:
            print('\n**INVALID PIN**\n')


def card_cvv():
    print('\nCVV SHOULD BE OF 3 DIGITS\n')
    while True:
        cvv = input('CVV : ')
        if check.cvv(cvv):
            return cvv
        else:
            print('\n**INVALID CVV**\n')


def reciever_account_number():
    acc_no = input('RECIVER ACCOUNT NUMBER : ')
    try:
        acc_no = int(acc_no)
        return acc_no
    except:
        print('\n**INVALID ACCOUNT NUMBER**\n')


def card_number():
    print('\nCARD NUMBER SHOULD BE OF TYPE INTEGER\n')
    card_number = input('CARD NUMBER : ')
    try:
        card_number = int(card_number)
        return card_number
    except:
        print('\n**INVALID CARD NUMBER**\n')


def card_type():
    print('\nONLY VISA, MASTERCARD, RUPAY\n')
    while True:
        card_type = input('CARD TYPE : ')
        if card_type.lower() == 'rupay' or card_type.lower() == 'mastercard' or card_type.lower() == 'visa':
            return card_type.lower()
        else:
            print('\n**INVALID CARD TYPE**\n')
