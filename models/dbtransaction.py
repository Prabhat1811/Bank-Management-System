'''
deals with transaction database
'''

import mysql.connector


class dbtransaction:

    @staticmethod
    def add_transaction(tran_amt, sender_acc_no, reciever_acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"INSERT INTO `bms`.`transaction` (`tranamt`,`senderaccno`,`recieveraccno`) VALUES ('{tran_amt}','{sender_acc_no}','{reciever_acc_no}');"

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
    def get_transaction(acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT * FROM `bms`.`transaction` WHERE `senderaccno`='{acc_no}'"
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
