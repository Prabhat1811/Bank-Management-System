'''
deals with card database
'''

import mysql.connector


class dbcard:

    @staticmethod
    def add_card(card_pin, card_cvv, card_type, acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"INSERT INTO `bms`.`card` (`cardpin`,`cardcvv`,`cardtype`,`accno`) VALUES ('{card_pin}','{card_cvv}','{card_type}','{acc_no}');"

        try:
            cur.execute(query)
            db.commit()
            cur.close()
            return True
        except:
            db.rollback()
            cur.close()
            return False

    @staticmethod
    def remove_card(card_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"DELETE FROM `bms`.`card` WHERE `cardno`='{card_no}'"
        try:
            cur.execute(query)
            db.commit()
            cur.close()
            return True
        except:
            cur.close()
            return False

    @staticmethod
    def verify_card(card_no, card_pin, card_cvv):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT cardpin FROM `bms`.`card` WHERE cardno = '{card_no}'  AND cardcvv='{card_cvv}'"
        cur.execute(query)

        try:
            result = cur.fetchone()[0]
            cur.close()
            if result == card_pin:
                return True
            return False
        except:
            cur.close()
            return False

    @staticmethod
    def get_cards(acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT cardno,cardtype FROM `bms`.`card` WHERE `accno`='{acc_no}'"
        cur.execute(query)

        try:
            result = cur.fetchall()
            cur.close()
            if len(result) > 0:
                return result
            return False
        except:
            cur.close()
            return False

    @staticmethod
    def get_account(card_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT accno FROM `bms`.`card` WHERE `cardno`='{card_no}'"
        cur.execute(query)

        try:
            result = cur.fetchone()
            cur.close()
            if len(result) > 0:
                return result[0]
            return False
        except:
            cur.close()
            return False
