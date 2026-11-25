from abc import ABC, abstractmethod

from Fundamentals import result


class Bank(ABC):
    @abstractmethod
    def atm(self):
        print("abstarct")

class card(Bank):
    def atm(self,balance):
        self.__balance = balance
        print("swipe the card")

    @property
    def inputt(self):
        try:
            user_amount = int(input("Enter your deposit amount:"))
            return user_amount
        except ValueError:
            print("system warning: letters detected! seting amouunt to 0")
            return 0

    def check_balance(self):
        if self.__balance < self.inputt:
            return self.__balance + 1000
        return self.__balance

class Deposit(Bank):
    @property
    def atm(self):
        # super().atm() if I don't use super then i cannot print abstract
        print("Enter your deposit amount")

b1 = Deposit()
b1.atm

c1 = card()
c1.atm(1000)

print(c1.check_balance())

class Employee:
    def __init__(self, name, salary):
        self.company = "TechCorp"
        self.name = name
        self.__salary = salary

    @property
    def salaryy(self):
        return self.__salary


c1 = Employee("john", 10000)
print(c1.name)
print(c1.company)
print(c1.salaryy)

class Employee:
    def __init__(self, name):
        self.name = name

    # def __str__(self):
    #     return f"Employee: {self.name}"

e1 = Employee("Arjun")
print(e1)

#Lambda functions..
variable = lambda x,y : x+y
print(variable(10,2))

b = lambda x: "even" if x%2==0 else "odd"
print(b(7))

dictt = [
    {"name" : "dinesh" , "salary" : 500000},
    {"name" : "akash"  , "salary" : 400000},
    {"name" : "rajni"  , "salary" : 300000},
    {"name" : "suraj"  , "salary" : 200000},
]

# result = sorted(dictt, key=lambda dictt : dictt["salary"])
# print(result)

result = [d["name"]for d in dictt ]
print(sorted(result))

listt = [4,5,7,8,96]
mapp = list(map(lambda x: x**2 , listt))
print(mapp)

listing = [5,1,2,3,6,9,7,4,5,8]
result = list(filter(lambda x: x>5,listing))
print(result)

nums = [12,2,3,4,5,6,9,8,7]
evens = [x for x in nums if x%2==0]
print(evens)

nums = [12,2,3,4,5,6,9,8,7]
evens = list(map(lambda x: x%2==0, nums))
print(evens)

import re

matter = "my name is dinesh and iam 24 year old i was born on 2002"
regex =  re.findall(r"\d+}",matter)
print(regex)

matter = "My name is dinesh and iam a software_engineer"
regex =  re.findall(r"[A-Za-z]+",matter)
print(regex)


# syntax for replacing
# re.sub(pattern(), replacement, text)

# re.findall() = for searching
# re.sub = for replacement

