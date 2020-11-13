from models.dbcustomer import dbcustomer


class customer:

    @staticmethod
    def get_id(cust_phone):
        return dbcustomer.get_id(cust_phone)

    @staticmethod
    def find_phone(cust_phone):
        return dbcustomer.find_phone(cust_phone)

    @staticmethod
    def find_email(cust_email):
        return dbcustomer.find_email(cust_email)

    @staticmethod
    def add_customer(cust_name, cust_email, cust_phone):
        return dbcustomer.add_customer(cust_name, cust_email, cust_phone)
