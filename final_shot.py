list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    if i%2==0:
        print(i)

def even(i):
    if i%2==0:
        return i
    else:
        return i
print(even(5))


names = ["Arun", "Bala", "Dinesh", "Charan"]
res = list(filter(lambda n: "a" in n.lower(), names))
print(res)

numss = [4,8,9,2,5,7]
res2 = list(filter(lambda n : n%2 ==0  , numss))
print(res2)


from functools import reduce
numbers = [5, 10, 15, 20]

res3 = reduce(lambda a,b : a+b, numbers)
print(res3)

numbers = [12, 5, 27, 8, 19, 3]
def larger_number(numbers):
    largest = numbers[0]
    second_largest = numbers[1]
    for n in numbers:
        if n > largest:
            largest = n
    return largest

print(larger_number(numbers))


numbers = [12, 5, 27, 8, 19, 3]
def is_even(num):
    if num % 2 == 0:
        return True
count = 0
total = 0
new = []
for n in numbers:
    if is_even(n):
        new.append(n)
        count += 1
        total += n
print(count)
print(total)

def main():
    print(is_even(4))
    a = 5+5
    return a
    print(is_even(4))
    # print(is_even)

def is_even(n):
    if n % 2 == 0:
        return True

print(main())

class test1():
    def __init__(self):
        print("Iam init1")

    @property
    def testing1(self):
        print("Iam testing1")
class test2(test1):
    def __init__(self):
        print("Iam init2")
        super().__init__()
    def testing2(self):
        print("Iam testing2")

obj = test2()
obj.testing1
obj.testing2()

class Greet:
    def greeting(self,name):
        self.name = name

    def returning(self):
        print("hi")

x = Greet()
x.greeting("Arun")

# class bank:
#     print("dinesh")
#     def __init__(self):
#         self.balance = 5000
#         print(self.balance)
#
#     # def execute(self):
#     #     print(self.balance)
#
# x = bank()
# # x.execute()

class bank:
    def __init__(self,balance):
        self.balance = balance

    def execute(self):
        print(self.balance)

x = bank(10000)
x.execute()

class bank:
    def __init__(self,balance,deposit):
        self.balance = balance
        self.deposit = deposit

    def execute(self,deposit):
        self.deposit += deposit
        print(self.balance)
        print(self.deposit)

x = bank(1000,14.580)
x.execute(12)

class bank:
    def __init__(self,balance,deposit):
        self.balance = balance
        self.deposit = deposit

    def execute(self):
        self.deposit += self.balance
        print(self.balance)
        print(self.deposit)


x = bank(1000,14.580)
x.execute()

class bank:
    def __init__(self):
        self.balance = 90000

    def execute(self):
        print(self.balance)

x = bank()
x.execute()
x.balance = 0
x.execute()

# THIS IS WITHOUT ENCAPSULATION
class Bank:
    def __init__(self):
        self.balance = 899
        self.amount_deposited = False
        # print(self.balance)

    def show_balance(self):
        print(self.balance)

    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited_amount = {amount}")
            self.amount_deposited = True
            self.show_balance()

    def withdraw(self, amount):
        if self.amount_deposited:
            self.balance = self.balance - amount
            self.show_balance()
        else:
            print(f"Deposited_amount = {amount}, So cannot withdraw")
            print("Enter again!")

obj_bank = Bank()
obj_bank.deposit(789)
# obj_bank.withdraw(-1)
obj_bank.withdraw(88)
print("----------------------------------------------------------")

# __balance → Double underscore వల్ల name mangling జరుగుతుంది.
# Outside నుంచి x1.__balance = 0 రాస్తే actual balance మారదు. కొత్త attribute ఏర్పడుతుంది.
# Actual balance మార్చడానికి class లో change_balance() లాంటి method రాయాలి.
# ఆ method ద్వారా validation కూడా చేయవచ్చు.

class Bank:
    def __init__(self):
        self.__balance = 899
        self.amount_deposited = False

    def show_balance(self):
        print(self.__balance)

    def deposit(self,amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Deposited_amount = {amount}")
            self.amount_deposited = True
            self.show_balance()

    def withdraw(self, amount):
        if self.amount_deposited:
            self.__balance = self.__balance - amount
            self.show_balance()
        else:
            print(f"Deposited_amount = {amount}, So cannot withdraw")
            print("Enter again!")

obj_bank = Bank()
obj_bank.show_balance()
#CHECKING/TRYING TO MAKE BALANCE 0
obj_bank.balance = 0
obj_bank.show_balance()
# Balance made 0 without encapsulation we can change the data..
print("-------------------------------")
# Now I'll put encapsulation and again try to change the balance..
obj_bank.balance = 0
obj_bank.show_balance()


#polymorphism
# Polymorphism means same method name, but different behaviour depending on the object.
# super() helps to print parents method also
class Employee:
    def work(self):
        print("I am working")
class Developer(Employee):
    def work(self):
        super().work()
        print("I am developer")

object = Developer()
object.work()

# Abstraction
# Abstraction means hiding implementation details and showing only the essential functionality to the user.
# The main purpose of Abstraction
# 1. Parent defines what a child must provide.
# 2. Child implements how it works.
# 3. The rest of your application can use different child objects through the same method.
# Parent = Rules
# Child = Implementation

from abc import ABC, abstractmethod

class Atm(ABC):
    @abstractmethod
    def withdraw(self):
        pass

class Sbi(Atm):
    def withdraw(self):
        print("I am sbi")

class Hdfc(Atm):
    def withdraw(self):
        print("I am Hdfc")

objj = Hdfc()
objj.withdraw()

def sum(a,b):
    return a+b
print(sum(10,5))

# It shows the differences between your latest committed version and your current file changes.
def difference(a,b):
    return a-b
print(sum(10,5))

def multiply(a,b):
    return a**b
print(multiply(10,5))