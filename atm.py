from abstract_bank import abstract_bank
from account import account
from card import card


class atm(abstract_bank):

    @staticmethod
    def get_account_number(card_no):
        return card.get_account(card_no)

    @staticmethod
    def access_account(card_no):
        acc_no = card.get_account(card_no)
        acc = account(acc_no)
        return acc

    @staticmethod
    def verify_account(acc_no):
        return account.find(acc_no)

    @staticmethod
    def verify_card(card_no, card_pin, card_cvv):
        return card.verify_card(card_no, card_pin, card_cvv)
