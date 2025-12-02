class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def view_balance(self):
        return f"На балансе {self.__balance} рублей!"


    def deposit_money(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Текущий баланс {self.__balance} успешно пополнен на {amount} рублей!"
        else:
            return f"Нельзя внести сумму, меньше, чем ноль!"

    def withdraw_money(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                return f"С баланса успешно снято {amount} рублей"
            else:
                return f"Недостаточно средств на балансе для вывода такой суммы ({amount}). Текущий баланс: {self.__balance}"
        else:
            return f"Нельзя вывести сумму, меньше, чем ноль!"


acc1 = BankAccount(1000)
print(acc1.view_balance())