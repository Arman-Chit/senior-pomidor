class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}: Баланс пополнен на {amount}. Новый баланс: {self._balance}")
        else:
            raise ValueError("Сумма пополнения должна быть положительной!")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счете!")
        self._balance -= amount
        print(f"{self.owner}: Снято {amount}. Текущий баланс: {self._balance}")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        print(f"{self.owner}: Начислены проценты {interest}. Новый баланс: {self._balance}")

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount
        print(f"{self.owner}: Овердрафт! Снято {amount}. Новый баланс: {self.get_balance()}")

savings = SavingsAccount("Arman", 100)
savings.deposit(500)
savings.withdraw(100)
savings.apply_interest()