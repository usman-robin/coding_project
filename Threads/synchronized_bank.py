class Const(object):
    MAX_ACCOUNT_LIMIT = 100000000.0
    MIN_ACCOUNT_LIMIT = 0.0

class CustomException(Exception):
    pass


class Bank(object):

    def __init__(self):
        self.balances = {}
        print (type(self.balances))

    def withdraw(self, account_number, amount):
        print("Taking {1} from account:{0}".format(account_number, amount))

        if account_number in self.balances:
            if self.balances[account_number] - amount < Const.MIN_ACCOUNT_LIMIT:
                raise Exception("Balance cannot be less than 0 after withdrawal")

            self.balances[account_number] -= amount
            print("Balance on the account after withdrawal is {}".format(self.balances[account_number]))
        else:
            raise Exception("Account number {}  does not exist".format(account_number))

    def deposit(self, account_number, amount):
        print("putting {1} to account:{0}".format(account_number, amount))
        #self.balances[2222] = 10
        if account_number not in self.balances:
            print("Im here in deposit")
            self.balances[account_number] = 0.0
        if (self.balances[account_number] + amount) > Const.MAX_ACCOUNT_LIMIT:
            raise Exception("Balance cannot be more than 100000000 after deposit")

        self.balances[account_number] += amount
        print("Balance on the account after deposit is {}".format(self.balances[account_number]))

    def transfer(self, to_account, from_account, amount):
        if amount < 0:
            raise Exception("Cannot transfer negative amounts")
        if to_account not in self.balances:
            print("Im here in deposit")
            self.balances[to_account] = 0.0

        self.withdraw(from_account, amount)
        self.deposit(to_account, amount)

        print("New balances {} : {}    {} : {}".format(from_account, self.balances[from_account],
                                                       to_account, self.balances[to_account]))

    def get_total_accounts_money(self):
        bal = 0
        #self.balances.
        for val in self.balances.values():
            bal += val
        return bal

rover = Bank()

rover.deposit(2222, 20)
rover.deposit(2221, 20)
rover.withdraw(2222, 10)
rover.transfer(1, 2221, 2)
print (rover.get_total_accounts_money())

