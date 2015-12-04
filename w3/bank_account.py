class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.history = ['Account was created']

    def deposit(self, amount):
        self.balance += amount
        message = 'Deposited {}'.format(amount)
        write_to_history(message)

    def balance(self):
        return self.balance

    def withdraw(self, amount):
        result = False

        if (self.balance - amount) >= 0:
            self.balance = self.balance - amount
            result = True
            message = 'Transfer from {0} {}'.format(self.name, amount)
            write_to_history(message)

        return result

    def __str__(self):
        message = "Bank account for {0} with balance of {1}{2}"
        return message.format(self.name, self.balance, self.currency)

    def __int__(self):
        return int(self.balance)

    def transfer_to(self, account, amount):
        result = False

        if self.currency == account.currency:
            account.balance += amount
            withdraw(amount)
            result = True
            message = 'Transfer to {0} for {1} {2}'.format(
                account, amount, self.currency)
            write_to_history(message)

        return result

    def write_to_history(self, message):
        self.history.append(message)
