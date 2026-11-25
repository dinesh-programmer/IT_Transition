import mainn
from mainn import square,is_even

def main():
    user = input("Enter your number")
    number = int(user)
    if number %2 == 0:
        def cube(number):
            return number ** 3
        print(cube(number))

    elif number %2 != 0:
        print(square(number))

main()

class test:
    def __init__(self):
        print("test")
    def method1(self):
        print("testmethod1")
class test2(test):
    def __init__(self):
        print("test2")
        super().__init__()
    def method2(self):
        print("methodtest2")
        super().method1()

obj = test2()
obj.method1()

#imported one
(is_even(5))

class Animal:
    def __init__(self):
        print("normal Animal")
class Dog(Animal):
    def sound(self):
        print("bow bow")

class Cat(Animal):
    def sound(self):
        print("meow meow")
# a = Animal()
d = Dog()
d.sound()
c = Cat()
c.sound()

class execution:
    def __init__(self):
        print("execution")

    def carmodel(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
x = execution()
x.carmodel("royal_enfield","bullet",1901)
print(x.year)

class Bank:
    bank_name = "SBI"
    def __init__(self,holder_name):
        self.holder_name = holder_name
    @classmethod
    def change_bank_name(cls,newname):
        cls.bank_name = newname

account1 = Bank("Arjun")
account2 = Bank("kiran")
print(account1.bank_name)
Bank.change_bank_name("HDFC")
print(Bank.bank_name)


from abc import ABC,abstractmethod
class Incred(ABC):
    @abstractmethod
    def emi(self):
        pass

class Finance(Incred):
    def emi(self):
        print("taken loan from incred")

class Bank(Incred):
    def emi(self):
        print("deposited loan from incred")

holder1 = Finance()
holder1.emi()

holder2 = Bank()
holder2.emi()


list = ["apple","orange","banana","pineapple","kiwi","dragon fruit"]
with open ("fileIO.py", "w") as doc:
    for fruit_list in list:
        file = doc.write("\n" + fruit_list)
        print(file)
