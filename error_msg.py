'''
prints different error messages
'''

import random


def error_messages():
    msg = ['\n**WOAH! SOMEONE FORGOT WHERE THE KEYS ARE**\n**TRY AGAIN**\n', '\n**YOU SHOULD PRACTICE TYPING**\n**INALID INPUT**\n', '\n**THATS PRETTY INVALID**\n',
           '\n**THATS AN INVALID INPUT**\n']

    return msg[random.randint(0, len(msg)-1)]


print(error_messages())
