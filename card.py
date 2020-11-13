from models.dbcard import dbcard


class card:

    @staticmethod
    def add_card(card_pin, card_cvv, card_type, acc_no):
        dbcard.add_card(card_pin, card_cvv, card_type, acc_no)

    @staticmethod
    def remove_card(card_no):
        dbcard.remove_card(card_no)

    @staticmethod
    def verify_card(card_no, card_pin, card_cvv):
        return dbcard.verify_card(card_no, card_pin, card_cvv)

    @staticmethod
    def get_cards(acc_no):
        return dbcard.get_cards(acc_no)

    @staticmethod
    def get_account(card_no):
        return dbcard.get_account(card_no)
