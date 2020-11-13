'''
main script
'''

from atm import atm
from bank import bank
import system
import my_input
import time

print('\n**WELCOME TO BANK MANAGEMENT SYSTEM**')
while True:
    choice1 = input('\n1.ATM\n2.BANK\n3.EXIT\n\nCHOICE : ')

    # ATM
    if choice1 == '1':
        while True:
            choice2 = input(
                '\n1.CASH WITHDRAWAL\n2.FUNDS TRANSFER\n3.BALANCE ENQUIRY\n4.MINI STATEMENT\nq TO GO TO MAIN MENU\n\nCHOICE : ')
            if choice2 == 'q' or choice2 == 'Q':
                break

            # WITHDRAWS AMOUNT FROM ACCOUNT
            elif choice2 == '1':
                info = system.login()
                acc = info[0]
                acc_no = info[1]
                amount = system.input_amount(acc)
                atm.cash_withdrawal(acc, amount)
                atm.add_transaction(amount, acc_no)
                time.sleep(0.2)
                print('\n**AMOUNT WITHDRAWED**\n')
                time.sleep(0.2)
                print('BALANCE : ', atm.balance_inquiry(acc))
                time.sleep(0.2)

            # TRANSFERS FUNDS TO OTHER ACCOUNT
            elif choice2 == '2':
                info = system.login()
                acc = info[0]
                acc_no = info[1]
                amount = system.input_amount(acc)
                acc_no_r = system.input_reviever_account()

                atm.fund_transfer(acc, acc_no_r, amount)
                atm.add_transaction(amount, acc_no, acc_no_r)
                time.sleep(0.2)
                print('\n**FUNDS TRANSFERED**\n')
                time.sleep(0.2)
                print('BALANCE : ', atm.balance_inquiry(acc))

            # SHOWS BALANCE IN ACCOUNT
            elif choice2 == '3':
                info = system.login()
                acc = info[0]
                time.sleep(0.2)
                print('\nBALANCE : ', atm.balance_inquiry(acc))

            # SHOWS ALL TRANSACTIONS TILL DATE
            elif choice2 == '4':
                info = system.login()
                acc_no = info[1]
                system.print_transactions(atm.mini_statement(acc_no))

            else:
                print('\n**INVALID CHOICE**\n')

    # BANK
    elif choice1 == '2':
        while True:
            choice2 = input(
                '\n1.OPEN ACCOUNT\n2.LOGIN ACCOUNT\n3.MAIN MENU\n\nCHOICE : ')
            if choice2 == '1':
                print('\n**OPEN ACCOUNT**\n')
                cust_id = system.add_customer()
                acc_no = system.add_account(cust_id)
                time.sleep(0.5)
                print('\n**ACCOUNT ADDED**\n')
                print('~'*50)
                print('\t\t\tIMPORTANT')
                print('\t\t\t---------')
                time.sleep(0.2)
                print('\nYOUR ACCOUNT NUMBER IS : ', acc_no)
                time.sleep(0.2)
                print('ACCOUNT BALANCE : 0')
                time.sleep(0.2)
                print(
                    '\nCURRENTLY THERE ARE NO CARDS LINKED TO YOUR ACCOUNT\nTO ADD CARD LOGIN TO YOUR ACCOUNT AND ADD CARD\n')
                print('~'*50)
            elif choice2 == '2':
                print('\n**LOGIN ACCOUNT**\n')
                acc_no = system.account_login()
                acc = bank.access_account(acc_no)
                time.sleep(0.5)
                print('\n**LOGIN SUCCESSFULL**\n')
                time.sleep(0.1)
                break
            elif choice2 == '3':
                break
            else:
                print('\n**INVALID CHOICE**\n')

        if choice2 == '2':
            while True:
                choice3 = input(
                    '\n1.ACCOUNT INFORMATION\n2.CASH WITHDRAWAL\n3.FUNDS TRANSFER\n4.BALANCE ENQUIRY\n5.MINI STATEMENT\n6.DEPOSIT AMOUNT\n7.ADD CARD\n8.SHOW CARDS\nq TO GO TO MAIN MENU\n\nCHOICE : ')
                if choice3 == 'q' or choice3 == 'Q':
                    break

                elif choice3 == '1':
                    system.print_acc_info(bank.get_info(acc))

                elif choice3 == '2':
                    amount = system.input_amount(acc)
                    bank.cash_withdrawal(acc, amount)
                    bank.add_transaction(amount, acc_no)
                    time.sleep(0.2)
                    print('\n**AMOUNT WITHDRAWED**\n')
                    time.sleep(0.2)
                    print('BALANCE : ', bank.balance_inquiry(acc))
                    time.sleep(0.2)

                elif choice3 == '3':
                    amount = system.input_amount(acc)
                    acc_no_r = system.input_reviever_account()
                    bank.fund_transfer(acc, acc_no_r, amount)
                    bank.add_transaction(amount, acc_no, acc_no_r)
                    time.sleep(0.2)
                    print('\n**FUNDS TRANSFERED**\n')
                    time.sleep(0.2)
                    print('BALANCE : ', bank.balance_inquiry(acc))
                    time.sleep(0.2)

                elif choice3 == '4':
                    print('\nBALANCE : ', bank.balance_inquiry(acc))

                elif choice3 == '5':
                    system.print_transactions(bank.mini_statement(acc_no))

                elif choice3 == '6':
                    amount = my_input.amount()
                    bank.deposit_money(acc_no, amount)
                    time.sleep(0.2)
                    print('\n**AMOUNT ADDED**\n')
                    time.sleep(0.2)
                    print('BALANCE : ', bank.balance_inquiry(acc))
                    bank.add_transaction(amount, acc_no, acc_no)
                    time.sleep(0.2)

                elif choice3 == '7':
                    print('\n**CARD DETAILS**\n')
                    card_pin = my_input.card_pin()
                    card_cvv = my_input.card_cvv()
                    card_type = my_input.card_type()

                    bank.add_card(card_pin, card_cvv, card_type, acc_no)
                    time.sleep(0.5)
                    print('\n**CARD ADDED SUCCESSFULLY**\n')

                elif choice3 == '8':
                    card_list = bank.get_cards(acc_no)
                    system.print_cards(card_list)

                else:
                    print('\n**INVALID CHOICE**\n')

    elif choice1 == '3':
        print('\nGOOD BYE,')
        time.sleep(0.1)
        print('PRABHAT BHARTOLA\n')
        time.sleep(1)
        break

    else:
        print('\n**INVALID CHOICE**\n')
