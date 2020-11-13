'''
deals with customer database
'''

import mysql.connector


class dbcustomer:

    @staticmethod
    def add_customer(cust_name, cust_email, cust_phone):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"INSERT INTO `bms`.`customer` (`custname`,`custemail`,`custphone`) VALUES ('{cust_name}','{cust_email}','{cust_phone}');"

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
    def get_id(cust_phone):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT custid FROM `bms`.`customer` WHERE `custphone`='{cust_phone}'"
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

    @staticmethod
    def find_phone(cust_phone):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT custphone FROM `bms`.`customer` WHERE `custphone`='{cust_phone}'"
        cur.execute(query)

        try:
            result = cur.fetchone()[0]
            cur.close()
            if result == cust_phone:
                return True
            return False
        except:
            cur.close()
            return False

    @staticmethod
    def find_email(cust_email):
        db = mysql.connector.connect(
            host='localhost', user='root', password='qwerty12345')

        cur = db.cursor()
        query = f"SELECT custemail FROM `bms`.`customer` WHERE `custemail`='{cust_email}'"
        cur.execute(query)

        try:
            result = cur.fetchone()[0]
            cur.close()
            if result == cust_email:
                return True
            return False
        except:
            cur.close()
            return False
