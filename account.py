from models.dbaccount import dbaccount


class account:
    def __init__(self, acc_no):
        self.acc_no = acc_no

    @staticmethod
    def add(acc_type, password, cust_id):
        return dbaccount.add_account(acc_type, password, cust_id)

    @staticmethod
    def verify(acc_no, password):
        return dbaccount.verify_account(acc_no, password)

    @staticmethod
    def find(acc_no):
        return dbaccount.find_account(acc_no)

    @staticmethod
    def deposit(acc_no, amount):
        return dbaccount.deposit(acc_no, amount)

    def withdraw(self, amount):
        return dbaccount.withdraw(self.acc_no, amount)

    def get_balance(self):
        return dbaccount.get_balance(self.acc_no)

    def deactivate(self):
        return dbaccount.deactivate(self.acc_no)

    def get_info(self):
        return dbaccount.get_info(self.acc_no)

    @staticmethod
    def get_accno(cust_id):
        return dbaccount.get_accno(cust_id)
