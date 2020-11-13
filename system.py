from atm import atm
from bank import bank
from customer import customer
from account import account
import my_input
import time


def insert_card():
    while True:
        card_no = my_input.card_number()
        card_pin = my_input.card_pin()
        card_cvv = my_input.card_cvv()
        if atm.verify_card(card_no, int(card_pin), int(card_cvv)):
            return card_no
        else:
            print('\n**INVALID DETAILS**\n')


def add_customer():
    print('\nCUSTOMER DETAILS\n')
    cust_name = my_input.username()
    while True:
        cust_phone = my_input.phone_number()

        if customer.find_phone(cust_phone):
            print('\n**PHONE ALREADY TAKEN**\n')
        else:
            break
    while True:
        cust_email = my_input.email()

        if customer.find_email(cust_email):
            print('\n**EMAIL ALREADY TAKEN**\n')
        else:
            break
    if customer.add_customer(cust_name, cust_email, cust_phone):
        return customer.get_id(cust_phone)
    else:
        return False


def add_account(cust_id):
    print('\nACCOUNT DETAILS\n')
    acc_type = my_input.account_type()
    password = my_input.password()

    if account.add(acc_type, password, cust_id):
        return account.get_accno(cust_id)
    else:
        return False


def account_login():
    while True:
        acc_no = input('ACCOUNT NUMBER : ')
        password = input('PASSWORD : ')

        if bank.verify_account(acc_no, password):
            return acc_no
        else:
            print('\n**ACCOUNT NOT FOUND**\n')


def input_amount(acc):
    while True:
        amount = my_input.amount()
        if atm.balance_inquiry(acc) < amount:
            print('\n**INSUFFICIENT FUNDS**\n')
            continue
        return amount


def input_reviever_account():
    while True:
        acc_no_r = my_input.reciever_account_number()
        if atm.verify_account(acc_no_r):
            return acc_no_r
        else:
            print('\n**ACCOUNT NOT FOUND**\n')


def login():
    print('\n**LOGIN**\n')
    card_no = insert_card()
    acc = atm.access_account(card_no)
    acc_no = atm.get_account_number(card_no)
    print('\n**LOGIN SUCCESSFULL**\n')
    return [acc, acc_no]


def print_transactions(tran_list):
    print('\n')
    if not tran_list:
        print('No Transactions\n')
        return

    print('TNo.  Date  Time  AMT  FROM  TO\n')
    [print(*line) for line in tran_list]


def print_cards(card_list):
    print('\n')
    time.sleep(0.1)
    if card_list == False:
        print('\n**THAERE ARE NO CARDS LINKED TO THIS ACCOUNT**\n**PRESS 7 TO ADD CARD**\n')
        return
    print('CARD NO.    TYPE\n')
    time.sleep(0.1)
    for i in card_list:
        print(i[0], end='           ')
        print(i[1].upper())


def print_acc_info(info):
    time.sleep(0.2)
    print('\n**ACCOUT INFORMATION**\n')
    time.sleep(0.5)
    print('ACCOUNT NUMBER : ', info[0])
    time.sleep(0.1)
    print('BALANCE : ', info[1])
    time.sleep(0.1)
    print('TYPE : ', info[2])
    time.sleep(0.1)
    print('STATUS : ', info[3])
    time.sleep(0.1)
    print('CUSTOMER ID : ', info[4])
    time.sleep(0.1)
    print('NAME : ', info[5])
    time.sleep(0.1)
    print('EMAIL ID : ', info[6])
    time.sleep(0.1)
    print('PHONE NUMBER :', info[7])
    time.sleep(0.1)
