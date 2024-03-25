import uuid


###########################################
####  Bank    #############################
####  Ido Sternhheim    ###################
###########################################


class Person:
    def __init__(self, private_name, family_name, age):
        self.private_name = private_name
        self.family_name = family_name
        self.age = age
        self.personId = str(uuid.uuid4())


class Customer(Person):
    def __init__(self, private_name, family_name, age=16):
        super().__init__(private_name, family_name, age)
        self.account = None

    def open_new_account(self):
        if self.account is None:
            self.account = Account(self.private_name, self.family_name, self.personId)
            print(f'New account has  open for: {self.private_name} {self.family_name}')
        else:
            print('You already has an account')


class Account:
    def __init__(self, private_name, family_name, personId):
        self.private_name = private_name
        self.family_name = family_name
        self.personId = personId
        self.accountId = uuid.uuid4()

    def __str__(self):
        return f'###################\nAccount Details:\nFirst name:\t{self.private_name}\nLast name:\t{self.family_name}\n###################'

    def __getitem__(self, personId):
        return [self.private_name, self.family_name, self.accountId, self.personId][personId]


Ido = Customer('ido', 'sternheim', 24)

Ido.open_new_account()
print(Ido.account)
