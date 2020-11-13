'''
abstract class for physical bank and atm
'''

from account import account
from transaction import transaction
from card import card


class abstract_bank:

    @staticmethod
    def fund_transfer(acc, acc_no_r, amount):
        if acc.withdraw(amount) and account.deposit(acc_no_r, amount):
            return True
        return False

    @staticmethod
    def cash_withdrawal(acc, amount):
        return acc.withdraw(amount)

    @staticmethod
    def cash_deposit():
        pass

    @staticmethod
    def balance_inquiry(acc):
        return acc.get_balance()

    @staticmethod
    def mini_statement(acc_no):
        return transaction.get(acc_no)

    @staticmethod
    def add_transaction(tran_amt, sen_acc_no, rec_acc_no=0):
        return transaction.add(tran_amt, sen_acc_no, rec_acc_no)

    @staticmethod
    def get_info(acc):
        return acc.get_info()

    @staticmethod
    def get_cards(acc_no):
        return card.get_cards(acc_no)
