class Bank:
    def __init__(self, name, initial_deposite, brance):
        self.name = name # Public
        self.branch = brance # Protected
        self.__balance = initial_deposite # Private

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


jabir = Bank("gamja", 100000,"Banani 11")

print(jabir.name)
jabir.deposite(400000)
# print(jabir.__balance)
print(jabir.get_balance())
print(jabir.branch)
# print(dir(jabir))
print(jabir._Bank__balance) 
