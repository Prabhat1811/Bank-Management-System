from abstract_bank import abstract_bank
from account import account
from card import card


class bank(abstract_bank):

    @staticmethod
    def open_account():
        pass

    @staticmethod
    def close_account():
        pass

    @staticmethod
    def change_phone_number():
        pass

    @staticmethod
    def cash_cheque():
        pass

    @staticmethod
    def deposit_cheque():
        pass

    @staticmethod
    def add_card(card_pin, card_cvv, card_type, acc_no):
        return card.add_card(card_pin, card_cvv, card_type, acc_no)

    @staticmethod
    def deposit_money(acc_no, amount):
        return account.deposit(acc_no, amount)

    @staticmethod
    def verify_account(acc_no, password):
        return account.verify(acc_no, password)

    @staticmethod
    def access_account(acc_no):
        acc = account(acc_no)
        return acc
