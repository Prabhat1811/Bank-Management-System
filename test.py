import unittest
from abstract_bank import abstract_bank
from account import account


class test_abstract_bank(unittest.TestCase):

    def setUp(self):
        self.acc = account('2')

    def test_fund_transfer(self):
        result = abstract_bank.fund_transfer(self.acc, '1', '100')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
