import string
import uuid
import time
import datetime
import os
import pickle

###########################################
####  Bank    #############################
####  Ido Sternhheim    ###################
###########################################

customers = {}


def save_files(_customers):
    try:
        with open(os.path.join(os.getcwd(), 'customers.p'), 'wb') as out:
            pickle.dump(_customers, out)
    except (IOError, pickle.PicklingError) as e:
        print(f"Error saving data: {e}")


def load_files():
    try:
        with open(os.path.join(os.getcwd(), 'customers.p'), 'rb') as f:
            return pickle.load(f)
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error loading data: {e}")
        return {}


class Person:
    def __init__(self, private_name, family_name, user_id, age):
        self.private_name = str(private_name).capitalize()
        self.family_name = str(family_name).capitalize()
        self.id = user_id
        self.age = age
        self.personId = str(uuid.uuid4())


class Customer(Person):
    def __init__(self, private_name, family_name, user_id, age='16'):
        super().__init__(private_name, family_name, user_id, age)
        self.account = None
        self.history = {}

    def deposit(self, sum_money: float, money_type: str = 'shekel'):
        time.sleep(1)
        now = datetime.datetime.now().strftime("%d:%m:%Y::%H:%M:%S")

        money_type = money_type.lower()
        money_types = ['shekel', 'euro', 'dollar']
        if money_type not in money_types:
            return f'This type of money does not exist, please use {money_types}'
        elif self.account.money_type == money_type:
            self.account.money += sum_money
            print(f'{self.private_name} deposit {sum_money} {money_type}')
            self.history[now] = f'deposit {sum_money} {money_type}'
        else:
            match self.account.money_type:
                case 'shekel':
                    if money_type == 'dollar':
                        self.account.money += sum_money * 3.67  # user insert dollars into shekel account
                        print(f'{self.private_name} deposit {sum_money} dollar -> {sum_money * 3.64} shekels')
                        self.history[now] = f'deposit {sum_money} dollar -> {sum_money * 3.64} shekels'
                    else:
                        self.account.money += sum_money * 3.97  # user insert euros into shekel account
                        print(f'{self.private_name} deposit {sum_money} euro -> {sum_money * 3.97} shekels')
                        self.history[now] = f'deposit {sum_money} euro -> {sum_money * 3.97} shekels'

                case 'dollar':
                    if money_type == 'shekel':
                        self.account.money += sum_money / 3.67  # user insert shekels into dollar account
                        print(f'{self.private_name} deposit {sum_money} shekel -> {sum_money / 3.67} dollar')
                        self.history[now] = f'deposit {sum_money} shekel -> {sum_money / 3.67} dollar'

                    else:
                        self.account.money += sum_money * 1.08  # user insert euros into dollar account
                        print(f'{self.private_name} deposit {sum_money} euro -> {sum_money * 1.08} dollar')
                        self.history[now] = f'deposit {sum_money} euro -> {sum_money * 1.08} dollar'

                case 'euro':
                    if money_type == 'shekel':
                        self.account.money += sum_money / 3.97  # user insert shekels into euro account
                        print(f'{self.private_name} deposit {sum_money} shekel -> {sum_money / 3.97} euro')
                        self.history[now] = f'deposit {sum_money} shekel -> {sum_money / 3.97} euro'

                    else:  # Dollar 3.64
                        self.account.money += sum_money / 1.08  # user insert dollars into euro account
                        print(f'{self.private_name} deposit {sum_money} dollar -> {sum_money / 1.08} euro')
                        self.history[now] = f'deposit {sum_money} dollar -> {sum_money / 1.08} euro'

    def withdraw(self, sum_money: float, money_type: str = 'shekel'):
        time.sleep(1)

        if sum_money > self.account.money:
            print(f'Unfortunately, you cannot withdraw {sum_money} because it exceeds your current account balance of {self.account.money}.')
            return
        now = datetime.datetime.now().strftime("%d:%m:%Y::%H:%M:%S")
        money_type = money_type.lower()
        money_types = ['shekel', 'euro', 'dollar']
        if money_type not in money_types:
            return f'This type of money does not exist, please use {money_types}'
        elif self.account.money_type == money_type:
            self.account.money -= sum_money
            print(f'{self.private_name} withdraw {sum_money} {money_type}')
            self.history[now] = f'withdraw {sum_money} {money_type}'

        else:
            match self.account.money_type:
                case 'shekel':
                    if money_type == 'dollar':
                        self.account.money -= (sum_money * 3.67)  # withdraw dollar from shekels account
                        print(f'{self.private_name} withdraw {sum_money} dollar -> {sum_money * 3.67} shekel')
                        self.history[now] = f'withdraw {sum_money} dollar -> {sum_money * 3.67} shekel'

                    else:
                        self.account.money -= (sum_money * 3.95)  # withdraw euro from shekels account
                        print(f'{self.private_name} withdraw {sum_money} euro -> {sum_money * 3.95} shekel')
                        self.history[now] = f'withdraw {sum_money} euro -> {sum_money * 3.95} shekel'

                case 'dollar':
                    if money_type == 'euro':
                        self.account.money -= (sum_money * 1.08)  # withdraw euro from dollars account
                        print(f'{self.private_name} withdraw {sum_money} euro -> {sum_money * 1.08} dollar')
                        self.history[now] = f'withdraw {sum_money} euro -> {sum_money * 1.08} dollar'

                    else:
                        self.account.money -= (sum_money / 3.67)  # withdraw shekels from dollars account
                        print(f'{self.private_name} withdraw {sum_money} shekel -> {sum_money / 3.67} dollar')
                        self.history[now] = f'withdraw {sum_money} shekel -> {sum_money / 3.67} dollar'

                case 'euro':
                    if money_type == 'shekel':
                        self.account.money -= sum_money / 3.97  # withdraw shekels from euro account
                        print(f'{self.private_name} withdraw {sum_money} shekel -> {sum_money / 3.97} euro')
                        self.history[now] = f'withdraw {sum_money} shekel -> {sum_money / 3.97} euro'

                    else:  # Dollar 3.64
                        self.account.money -= sum_money / 1.08  # withdraw dollar from euro account
                        print(f'{self.private_name} withdraw {sum_money} dollar -> {sum_money / 1.08} euro')
                        self.history[now] = f'withdraw {sum_money} dollar -> {sum_money / 1.08} euro'

    def __str__(self):
        return f'{self.id}: {self.private_name} {self.family_name} {self.age} years old'


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

    def change_account_type(self):
        money_types = ['shekel', 'euro', 'dollar']
        money_types.remove(self.money_type)
        answer = str(input('Are you sure you want to change account type? [y or n]')).lower()
        while answer != 'y' and answer != 'n':
            answer = str(input('Are you sure you want to change account type? [y or n]')).lower()
        if answer == 'n':
            return
        print(f'Account type is {self.money_type}')
        answer = str(input(f'Which type do you want? [{money_types}]')).lower()
        while answer not in money_types:
            print(f'Sorry, this is not an option')
            answer = str(input(f'Which type do you want? [{money_types}]')).lower()

        match answer:
            case 'shekel':
                if self.money_type == 'dollar':
                    self.money *= 3.67
                    self.money_type = 'shekel'
                else:
                    self.money *= 3.97
                    self.money_type = 'shekel'
            case 'euro':
                if self.money_type == 'dollar':
                    self.money /= 1.08
                    self.money_type = 'euro'
                else:
                    self.money /= 3.97
                    self.money_type = 'euro'
            case 'dollar':
                if self.money_type == 'euro':
                    self.money *= 1.08
                    self.money_type = 'dollar'
                else:
                    self.money /= 3.67
                    self.money_type = 'dollar'
        print(f'Account change to {answer}')


def is_user_exist(id):
    customers = load_files()
    try:
        if customers[str(id)]:
            return True
    except:
        return False


def account_menu(user_id):
    while True:
        print('\n\n[1] Withdraw\n[2] Deposit\n[3] Show Amount\n[8] Change Account Type\n[9] Quit')
        step3 = input('What do you want to do today: ')
        while step3 != '1' and step3 != '2' and step3 != '3' and step3 != '9' and step3 != '8':
            step3 = input('\n\nNot valid input, What do you want to do today: ')
        match step3:
            case '1':
                money_types = ['shekel', 'euro', 'dollar']
                money_type = str(input(f'\nwhich type of money [{",".join(money_types)}]:')).lower()
                while money_type not in money_types:
                    print('\nSorry, this type of money does not exist')
                    money_type = input(f'\nwhich type of money [{",".join(money_types)}]:')
                money_ok = False
                money_withdraw = 0
                while not money_ok:
                    money_withdraw = input('\nHow much money do you want to withdraw: ')
                    if not money_withdraw.isdigit():
                        print('Sorry, you can not withdraw it')
                        continue
                    if float(money_withdraw) < 0:
                        print('Sorry, you can not withdraw less than 0')
                    money_ok = True

                customers[user_id].withdraw(float(money_withdraw), money_type)
                save_files(customers)

            case '2':
                money_types = ['shekel', 'euro', 'dollar']
                money_type = str(input(f'\nwhich type of money [{",".join(money_types)}]:')).lower()
                while money_type not in money_types:
                    print('\nSorry, this type of money does not exist')
                    money_type = input(f'\nwhich type of money [{",".join(money_types)}]:')
                money_ok = False
                money_withdraw = 0
                while not money_ok:
                    money_withdraw = input('\nHow much money do you want to deposit: ')
                    if not money_withdraw.isdigit():
                        print('Sorry, you can not deposit it')
                        continue
                    if float(money_withdraw) < 0:
                        print('Sorry, you can not deposit less than 0')
                    money_ok = True

                customers[user_id].deposit(float(money_withdraw), money_type)
                save_files(customers)

            case '3':
                print(customers[user_id].account)
            case '8':
                customers[user_id].account.change_account_type()
            case '9':
                return


def login_menu(user_id):
    print(f'\n\n#### Welcome {customers[user_id].private_name} {customers[user_id].family_name} ####')
    if customers[user_id].account is None:

        while True:
            print('[1] Create Bank Account\n[2] Show Me Details\n[3] Quit')
            step2 = input('What do you want to do today: ')
            while step2 != '1' and step2 != '2' and step2 != '3':
                step2 = input('Not valid input, What do you want to do today: ')
            match step2:
                case '1':
                    money_types = ['shekel', 'euro', 'dollar']
                    money_type = str(input(f'\nwhich type of money [{",".join(money_types)}]:')).lower()
                    while money_type not in money_types:
                        print('Sorry, this type of monet does not exist')
                        money_type = input(f'\nwhich type of money [{",".join(money_types)}]:')

                    customers[user_id].account = Account(customers[user_id].private_name,
                                                         customers[user_id].family_name,
                                                         customers[user_id].personId, money_type)
                    print(
                        f'\nNew bank account has open for: {customers[user_id].private_name} {customers[user_id].family_name}\n')
                    save_files(customers)
                    account_menu(user_id)
                    return
                case '2':
                    print(customers.get(user_id))
                case '3':
                    return

    else:
        account_menu(user_id)
        save_files(customers)


while True:
    customers = load_files()
    print(f'\nWelcome to the Bank')
    print('[1] for login\n[2] for register\n[9] exit')
    step1 = str(input('What do you want to do: '))
    while step1 != '1' and step1 != '2' and step1 != '9':
        step1 = str(input('Wrong input, try again: '))
    match step1:
        case '9':
            print('\nGoodBye!')
            save_files(customers)
            break
        case '1':
            login = input('\nEnter ID: ').strip()
            try:
                if customers[login]:
                    login_menu(login)
                else:
                    print('\nNot exist')
            except Exception as e:
                print(e)

        case '2':
            id = input('ID: ').strip()
            while len(str(id)) != 9:
                id = input("ID [9 digits]: ").strip()
            if is_user_exist(id):
                print('this ID already exist')
                continue
            fname = str(input('First Name: ')).strip()
            lname = str(input('Last Name: ')).strip()
            age = input('Age: ').strip()
            customers[id] = Customer(fname, lname, id, age)
            login_menu(id)

    save_files(customers)
