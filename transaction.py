from models.dbtransaction import dbtransaction


class transaction:

    @staticmethod
    def add(tran_amt, sen_acc_no, rec_acc_no):
        return dbtransaction.add_transaction(tran_amt, sen_acc_no, rec_acc_no)

    @staticmethod
    def get(acc_no):
        return dbtransaction.get_transaction(acc_no)
