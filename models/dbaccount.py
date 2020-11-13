'''
deals with account database 
'''

import mysql.connector


class dbaccount:

    @staticmethod
    def add_account(acc_type, password, cust_id):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"INSERT INTO `bms`.`account` (`acctype`,`password`,`custid`) VALUES ('{acc_type}','{password}','{cust_id}');"

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
    def verify_account(acc_no, password):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT password FROM `bms`.`account` WHERE accno = '{acc_no}' and status = 'active'"
        cur.execute(query)

        try:
            result = cur.fetchone()[0]
            cur.close()
            if result == password:
                return True
            return False
        except:
            cur.close()
            return False

    @staticmethod
    def find_account(acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT * FROM `bms`.`account` WHERE `accno`='{acc_no}' and `status`='active'"
        cur.execute(query)

        try:
            result = cur.fetchone()
            cur.close()
            if len(result) > 0:
                return True
            return False
        except:
            cur.close()
            return False

    @staticmethod
    def deposit(acc_no, amount):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"UPDATE `bms`.`account` SET accamt=accamt+{amount} WHERE accno={acc_no}"
        try:
            cur.execute(query)
            db.commit()
            cur.close()
            return True
        except:
            cur.close()
            return False

    @staticmethod
    def withdraw(acc_no, amount):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"UPDATE `bms`.`account` SET accamt=accamt-{amount} WHERE accno={acc_no}"
        try:
            cur.execute(query)
            db.commit()
            cur.close()
            return True
        except:
            cur.close()
            return False

    @staticmethod
    def get_balance(acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT accamt FROM `bms`.`account` WHERE `accno`='{acc_no}'"
        cur.execute(query)

        try:
            result = cur.fetchone()[0]
            cur.close()
            return result
        except:
            cur.close()
            return False

    @staticmethod
    def deactivate(acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"UPDATE `bms`.`account` SET status='inactive' WHERE accno={acc_no}"
        try:
            cur.execute(query)
            db.commit()
            cur.close()
            return True
        except:
            cur.close()
            return False

    @staticmethod
    def get_info(acc_no):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT `accno`,`accamt`,`acctype`,`status`,`customer`.`custid`,`custname`,`custemail`,`custphone` FROM `bms`.`account` INNER JOIN `bms`.`customer` ON `account`.`custid`=`customer`.`custid` WHERE `accno`='{acc_no}'"
        cur.execute(query)

        try:
            result = cur.fetchall()[0]
            cur.close()
            return result
        except:
            cur.close()
            return False

    @staticmethod
    def get_accno(cust_id):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT accno FROM `bms`.`account` WHERE `custid`='{cust_id}'"
        cur.execute(query)

        try:
            result = cur.fetchone()[0]
            cur.close()
            return result
        except:
            cur.close()
            return False
