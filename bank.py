import pprint

class Const(object):
    MAX_ACCOUNT_LIMIT = 100000000.0
    MIN_ACCOUNT_LIMIT = 0.0

class CustomException(Exception):
    pass


class Bank(object):

    def __init__(self):
        self.balances = {}
        #print (type(self.balances))

    def withdraw(self, account_number, amount):
        print("Taking {1} from account in withdraw:{0}".format(account_number, amount))

        if account_number in self.balances:
            if self.balances[account_number] - amount < Const.MIN_ACCOUNT_LIMIT:
                raise Exception("Balance cannot be less than 0 after withdrawal")

            self.balances[account_number] -= amount
            print("Balance on the account after withdrawal is {}".format(self.balances[account_number]))
        else:
            raise Exception("Account number {}  does not exist".format(account_number))

    def deposit(self, account_number, amount):
        #print("putting {1} to account:{0}".format(account_number, amount))

        if account_number not in self.balances:
            #print("Im here in deposit")
            self.balances[account_number] = 0.0
        if (self.balances[account_number] + amount) > Const.MAX_ACCOUNT_LIMIT:
            raise Exception("Balance cannot be more than 100000000 after deposit")

        self.balances[account_number] += amount
        #print("Balance on the account after deposit is {}".format(self.balances[account_number]))

    def transfer(self, to_account, from_account, amount):
        if amount < 0:
            raise Exception("Cannot transfer negative amounts")

        if from_account not in self.balances:
            raise Exception("Cannot transfer from a non existant account")

        if to_account not in self.balances:
            print("Opening a new account because account does not exist")
            self.balances[to_account] = 0.0

        deposit_succesful = False
        self.withdraw(from_account, amount)

        try:
            self.deposit(to_account, amount)
            deposit_succesful = True
        finally:
            # Try Finally clause to make sure to rollback the amount if error happens in the deposit
            if not deposit_succesful:
                print("In rollback")
                self.deposit(from_account, amount)
                pprint.pprint(self.balances)

        print("New balances {} : {}    {} : {}".format(from_account, self.balances[from_account],
                                                       to_account, self.balances[to_account]))

    def get_total_accounts_money(self):
        bal = 0
        for val in self.balances.values():
            bal += val
        return bal

    def print_account_numbers_balances(self):
        return self.balances


bnk = Bank()

bnk.deposit(1, 20)
bnk.deposit(3, 99999999)
#bnk.withdraw(1, 10)
bnk.transfer(3, 1, 5)
#bnk.transfer(4, 1, 5)


print (bnk.get_total_accounts_money())
pprint.pprint(bnk.print_account_numbers_balances())


"""
Test Cases:


Smoke Tests:
: Create a new account with deposit method
: Create new account with transfer method
: take out money using withdraw method

Sanity Tests:
Pick any one of the smoke tests

Functional Tests:
: withdraw money from a non existant account should fail -ve
: transfer money from a non existant account should fail -ve
: Test rollback by opening account with 99999999 and transfering 2 more to it (boundary)
: Test max and min limits (boundary)
: Create 2 accounts with deposit and transfer money between those accounts
: Total money for bank is same as 1 account
: Transfers should not change total bank money
: transfer money to a non existent account should succeed and create a new to_account
: Total amount of money in an Empty bank is 0
: Add money using deposit and transfer to an existing account



System Tests:
Create n threads accounts totaling a balance x and transfer money to each other total balance
should not change, run for a few hours


Performance Tests:
calculate times fr bank account transfer baseline and make sure the time is not changing
with every new checkin

"""