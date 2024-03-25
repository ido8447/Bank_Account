import string
import uuid


###########################################
####  Bank    #############################
####  Ido Sternhheim    ###################
###########################################


class Person:
    def __init__(self, private_name, family_name, age):
        self.private_name = str(private_name).capitalize()
        self.family_name = str(family_name).capitalize()
        self.age = age
        self.personId = str(uuid.uuid4())


class Customer(Person):
    def __init__(self, private_name, family_name, age=16):
        super().__init__(private_name, family_name, age)
        self.account = None

    def open_new_account(self):
        if self.account is None:
            money_types = ['shekel', 'euro', 'dollar']
            money_type = str(input(f'which type of money [{",".join(money_types)}]:')).lower()
            while money_type not in money_types:
                print('Sorry, this type of monet does not exist')
                money_type = input(f'which type of money [{",".join(money_types)}]:')

            self.account = Account(self.private_name, self.family_name, self.personId, money_type)
            print(f'New bank account has open for: {self.private_name} {self.family_name}')
        else:
            print('You already has an account')

    def deposit(self, sum_money: float, money_type: str = 'shekel'):
        money_type = money_type.lower()
        money_types = ['shekel', 'euro', 'dollar']
        if money_type not in money_types:
            return f'This type of money does not exist, please use {money_types}'
        elif self.account.money_type == money_type:
            self.account.money += sum_money
            print(f'{self.private_name} deposit {sum_money} {money_type}')

        else:
            match self.account.money_type:
                case 'shekel':
                    if money_type == 'dollar':
                        self.account.money += sum_money * 3.64  # user insert dollars into shekel account
                        print(f'{self.private_name} deposit {sum_money} dollar -> {sum_money * 3.64} shekels')
                    else:
                        self.account.money += sum_money * 3.95  # user insert euros into shekel account
                        print(f'{self.private_name} deposit {sum_money} euro -> {sum_money * 3.95} shekels')

                case 'dollar':
                    if money_type == 'shekel':
                        self.account.money += sum_money / 3.64  # user insert shekels into dollar account
                        print(f'{self.private_name} deposit {sum_money} shekel -> {sum_money / 3.64} dollar')

                    else:
                        self.account.money += sum_money * 1.08  # user insert euros into dollar account
                        print(f'{self.private_name} deposit {sum_money} euro -> {sum_money * 1.08} dollar')

                case 'euro':
                    if money_type == 'shekel':
                        self.account.money += sum_money * 0.25  # user insert shekels into euro account
                        print(f'{self.private_name} deposit {sum_money} shekel -> {sum_money * 0.25} euro')

                    else:  # Dollar 3.64
                        self.account.money += sum_money * 0.92  # user insert dollars into euro account
                        print(f'{self.private_name} deposit {sum_money} dollar -> {sum_money * 0.92} euro')


class Account:
    def __init__(self, private_name, family_name, personId, money_type='shekel'):
        self.private_name = private_name
        self.family_name = family_name
        self.personId = personId
        self.accountId = uuid.uuid4()
        self.money_type = money_type.lower()
        self.money = 0

    def __str__(self):
        return f'###################\nAccount Details:\nFirst name:\t{self.private_name}\nLast name:\t{self.family_name}\nMoney:\t{self.money} {string.capwords(self.money_type)}\n###################'

    def __getitem__(self, personId):
        return [self.private_name, self.family_name, self.accountId, self.personId][personId]


Ido = Customer('ido', 'sternheim', 24)
Ido.open_new_account()
print(Ido.account)
Ido.deposit(100)
Ido.deposit(100, 'shekel')
Ido.deposit(100, 'dollar')
Ido.deposit(100, 'EURO')
print(Ido.account)

