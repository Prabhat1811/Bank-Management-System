import re

'''
Other important functions
'''


def username(username):
    pattern = re.compile(
        r'(?=.*[a-z]+)(?=.*[A-Z]*)(?=.*[0-9]*)[a-zA-Z0-9]{3,}')
    try:
        string = re.search(pattern, username)[0]
        if string == username:
            return True
        return False
    except:
        return False


def phone_number(phone_number):
    pattern = re.compile(r'\d{10}')
    try:
        string = re.search(pattern, phone_number)[0]
        if string == phone_number:
            return True
        return False
    except:
        return False


def email_id(email_id):
    pattern = re.compile(r'[a-zA-Z0-9]{2,}@[a-z0-9]+\.[a-zA-Z]+')
    try:
        string = re.search(pattern, email_id)[0]
        if string == email_id:
            return True
        return False
    except:
        return False


def password(password):
    pattern = re.compile(
        r'(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[!@#$%^&*]+)[a-zA-Z0-9!@#$%^&*]{8,}')

    try:
        string = re.search(pattern, password)[0]
        if string == password:
            return True
        return False
    except:
        return False


def pin(pin):
    pattern = re.compile(r'\d{4}')
    try:
        string = re.search(pattern, pin)[0]
        if string == pin:
            return True
        return False
    except:
        return False


def cvv(cvv):
    pattern = re.compile(r'\d{3}')
    try:
        string = re.search(pattern, cvv)[0]
        if string == cvv:
            return True
        return False
    except:
        return False
