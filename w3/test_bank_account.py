import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("Rado", 1000, "$")

    def test_account_init(self):
        self.assertEqual(self.account.name, "Rado")
        self.assertEqual(self.account.balance, 1000)
        self.assertEqual(self.account.currency, "$")

    def test_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 1050)



if __name__ == '__main__':
    unittest.main()