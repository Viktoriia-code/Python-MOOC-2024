class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, summa: float):
        self.__balance += summa
        self.__service_charge()

    def withdraw(self, summa: float):
        self.__balance -= summa
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance = self.__balance - self.__balance * 0.01


