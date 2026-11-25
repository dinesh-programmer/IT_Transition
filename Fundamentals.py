

print("IT transition in 16 weeks")
print("Function and Variables")
# name = input("what's your name?")
# print("hello",name)
# print("hello"+"", name)

# print("my name is ", name)
# print(f"my name is {name}")
print("   hello dinesh   ")
name = "   nama dinesh   "
print(name.strip().replace(" ",""))

def exp():
    x = 87.5
    y = 117.651
    a = x+y
    return a
print(exp())

def printing():
    greet = "   namasthe dinesh  "
    new_greet = greet.strip().title()
    return new_greet
print(printing())

def printing():
    greet = "   hello world  "
    return greet.strip().replace(" ","")
print(printing())

x = 68.1
print(round(x))
print(f"{round(x)}")

y = 68.1789
print(round(y,2))

def hello(name):
    return name
print("hello",name)

(hello("nama"))


# def sub(a,b):
#     return a-b
#
# def result():
#   a =  int(input("whats a?"))
#   b =  int(input("whats b?"))
#   return sub(a,b)
# print(result())

def sub2(a,b):
    return a-b
print(sub2(10,20))

def calci(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
    print(a%b)
    print(a**b)
    return a,b
calci(10,20)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a//b

result = div(10,20)
print(result)

# Practice

def hello():
    print("helloworld")
hello()

def greet(name):
    return f"Hello {name}"
print(greet("nama"))

def sum():
    a = 2
    b = 3
    return a+b
print(sum())

def details():
    name ="nama"
    age = 24
    print(name,age)

details()

def total():
    x = 47
    y = 89
    z = 74
    return x+y+z
print(total())

# def total_price():
#     price = 10
#     quantity = 5
#     combined = price*quantity
#     return combined
# print(total_price())

# Function to funtion with user input...
# def total_price(price,quantity):
#     return  price * quantity
#
# def costs():
#     price = int(input("enter the price"))
#     quantity= int(input("enter the quantity"))
#     return total_price(price,quantity)
#
# print(costs())

# Funtion to Funtion with funtion call...
# def total_price(price,quantity):
#     return  price * quantity
#
# def costs(price,quality):
#     return total_price(price,quality)
#
# print(costs(42,8))

#Normal function..
def total_price():
    price = 100
    quantity = 3.5
    return  price * quantity

print(total_price())

def math():
    a = 88
    b =99
    return a//b, a%b, a**b
print(math())

def squ():
    x = 2
    return x**2
print(squ())

# level-2
# def greeting():
#     name = input("what is your name?")
#     return f"{name}, how are you?"
# print(greeting())

# def asking_user():
#     x1 = int(input("give your first number"))
#     x2 = int(input("give your second number"))
#     print(f"{x1}\n{x2} \n total= {x1+x2}")
# asking_user()

def store():
    out = "  hello world  "
    print(f"{out.strip().replace(" ","")}")
store()

def storing():
    course = "python programming"
    print(f"{course.replace("python","java")}")
storing()

# def take():
#     name = input("what is your name?")
#     age = int(input("what is your age?"))
#     print(f"my name is {name} and I am {age}years old")
# (take())

def sentence():
    text = "iam learning python"
    print(f"{text.strip().replace(" ","-")}")
sentence()

def calculation():
    a = 55
    b = 98
    print(f"{a} + {b} = {a+b}---as simple as that")
calculation()

z = 68.1789
print(round(z,2))

def seperation():
    word1 = "hello"
    word2 = "world"
    print(f"{word1}{word2}")
seperation()

def seperation():
    word1 = "hello"
    word2 = "world"
    print(word1,word2, sep="-")
    # print(f"{word1}-{word2}")
seperation()

def values():
    print("apple","banana","orange", sep="\n")

values()

num = 52.6855
print(f" {round(num,2)}")

def hello():
    print("hello")
hello()

def square(n):
    return n**3
print(square(5))

def add(a,b):
    return a+b

print(add(5,6))
print(add(10,11))

def nums(a=4,b=78):
    add = a+b
    return add
print(nums())

def  take(name):
    return name
print(take("nama"))

# Parameters and Arguments
# Define a function with parameters a and b, then call it using variables x and y.
def reverse(a,b):
    return a+b

x= 20
y= 50
result = reverse(x,y)
print(result)

def add(a,b):
    return a+b

num1 = 54
num2 = 78
totalnums = add(num1,num2)
print(totalnums)

# def user():
#     ask = input("what's the topic?")
#     return ask
# print(user())

def cube(n=10):
    return n*n*n
print(cube())

# def default(a=20.25,b):
#     return a+b
# print(default(1.8,4))

def default(a,b=7410):
    return a+b
print(default(1))

def default(a=20.25,b=87):
    return a+b
print(default())

def default(a=44,b=36):
    return a+b
print(default(1.8,4))


def override(a=69):
    return a+10
print(override(78))

#Function inside Function
def square(n):
    return n**2

def result(n):
    return square(n)
print(result(4))

def mul(a,b):
    return a*b

# def result():
#     input1 = int(input("enter 1st number"))
#     input2 = int(input("enter 2nd number"))
#     # return f"{input1}\n{input2}"  # for one down other
#     return mul(input1,input2)
#
# print(result())

def rounded(n):
    return round(n,2)
print(rounded(4.288))

# def clean():
#     name = input("what is your name?")
#     return name.strip().replace(" ","-")
#
# print(clean())

def send(x,y):
    return x+y

def receiver(a,b):
    a = send(1,0)
    return a

# one = 20
# two = 8
print(receiver(x,y))

def even(n):
    if n%2 == 0:
        return n
def collection(n):
    if n == even(n):
        return n+5

(collection(2))



def square(n):
    # if n%2 == 0:
        return n**2
def evens(n):
    if n%2 == 0:
        print(square(n))
        return n
(evens(2))

def double(n):
    if n%2 == 0:
        return n**2
    else:
        print("its odd baby")
print(double(8))

def double(n):
    if n%3 == 1:
        return n+5
    else:
        print("its even baby")

def add_five(n):
        print(double(n))
(add_five(7))

def odd(n):
    if n%3 == 1:
        return n - 3
def ans(n):
    if n-3 == odd(n):
        print(odd(n))
(ans(4))

def even(n):
    if n%2 == 0:
        return n +10
def collection(n):
    if n +10 == evens(n):
        print(evens(n))
collection(88)

# def age():
#     person = int(input("enter your age"))
#     if person < 18:
#         print("you're not an adult")
#     else:
#         print(f"iam {person} years old")
#         return person
#
# (age())

# def get_number():
#     ask = input("enter your favourite number")
#     print(f"my favourite number is {ask}")
#     return ask
# get_number()

# here used th euser input in the function itself

# def add_numbers(a,b):
#     return a+b
# def ask_user():
#     print(add_numbers())
#     x = int(input("enter the number1"))
#     y = int(input("enter the number2"))
# ask_user()

# def add_numbers(a,b):
#     return a+b
# def ask_user(x,y):
#     print(add_numbers(x,y))
#
# x = int(input("enter the number1"))
# y = int(input("enter the number2"))
# ask_user(x,y)

# user enters number
#        ↓
# function A receives/returns it
#        ↓
# function B checks whether it is even
#        ↓
# if even → add 5
#        ↓
# return final result
#        ↓
# print

# def user(num):
#     if num%2 == 0:
#         return num +5
# def even_number():
#     x = int(input("enter the number"))
#     return (user(x))
#
# print(even_number())

# user enters two numbers
#        ↓
# function gets them
#        ↓
# another function adds them
#        ↓
# another function checks whether the sum is greater than 50
#        ↓
# return the appropriate result
#        ↓
# print

# def get_numbers():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     return a, b
#
# def add(a, b):
#     return a + b
#
# def check(total):
#     if total > 50:
#         return "Greater than 50"
#     else:
#         return "50 or less"
#
# def result():
#     a,b = get_numbers()
#     total = add(a, b)
#     return check(total)
#
# print(result())

i = 3
while i!=0:
    print("meow")
    i=i-1

print("bow\n" *3)
print("bow" *3)

n = 0
while True:
    if n == 3:
        break
    print(n)
    n+=1

    for _ in range(n):
        print("I will stop")
i = 0

while i < 4:
    print(i)
    i += 2

i = 0
while i <= 5:
    print(i)
    i += 1


i = 1
while i<10:

    i+=1
    if i%2 !=0:

        print(i)

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)

    i += 1
print("------------------------")
# while True:
#     i = int(input("enter i"))
#     if i % 2 == 0:
#         print(i)
#         break
#     else:
#         print("that's odd")
# print("---------------------")

# list  = [2,1,3,4,5,6,7,8,9,5,8,9,3,4,7,1,2,5,6,3]
# for i in list:
#     if i%2==0:
#         if i>2:
#             print(i)
#
# for i in range(10):
#     print(i,i+1)

#okay I just want to print a table that should be even number
# i = 1
# n = int(input("enter n value - "))
# while i<11:
#     if n%2 ==0:
#         print(n, "*" , i ,"=" , n*i)
#         i+=1
#     else:
#         break
# Asking user to print from that list
# list = [1,2,3,4,5,6,7,8,9]
# i = 1
# x = int(input("fetch me a number from the list"))
#
# if x in  list:
#     while i<11:
#         print(x,"*", i, "=" ,x*i)
#         i+=1
# else:
#     print("not found")

#Asking user to take an even number from the list and print the table

# list = [1,2,3,4,5,6,7,8,9]
# i = 1
# x = int(input("fetch me a number from the list:"))
# if x in  list:
#     if x%2==0:
#         while i<11:
#             print(x,"*", i, "=" ,x*i)
#             i+=1
#     else:
#         print("Not an even number i think so!")
# else:
#     print("not found")

i= 0
empty = []
largest = []
nums = [22,55,44,88,77,99,66,3,69]
while i <len(nums):
    if nums[i]>40:
        (empty.append(nums[i]))
    i+=1

i = 0
largest = empty[0]

while i < len(empty):
    if empty[i] > largest:
        largest = empty[i]
    i += 1

print(largest)
print("----------------------")

i = 0
while i<11:
    print(i)
    i+=1
print("----------------------")

x = 0
while x > 10:
    print(x)
    i-=1
print(x)
print("---------------------")

i = 1
while i<21:
    if i%2==0:
        print(i)
    i+=1
print("---------------------")

i = 0
numbers = [4, 9, 2, 17, 6, 21, 8]
while i < len(numbers):
    if numbers[i] > 10:
        print(i,numbers[i])
    i+=1
print("---------------------")


i=0
larger =numbers[0]
numbers = [12, 5, 27, 8, 19, 3]
while i < len(numbers):
    if numbers[i] > larger and numbers[i] % 2 == 0:
        larger = numbers[i]
    i+=1

print(larger)

i = 0
nums = [77,88,99,44,55,66,11,32,25]
smaller  = nums[i]
while i< len(nums):
    if nums[i] < smaller:
        smaller = nums[i]
    i+=1

print(smaller)


# def square(n):
#     return n ** 2
# def asking_user():
#     n = int(input("give me a number"))
#     while n !=0:
#         if n%2 == 0:
#             print(square(n))
#             break
#         else:
#             print("Odd")
#         n = int(input("give me a number"))
# asking_user()



# def positive_square(x):
#     return x ** 2
#
#
# def check(x):
#     if x > 0:
#         return positive_square(x)
#     elif x < 0:
#         return "Negative"
#     else:
#         return "Zero"
#
# def user():
#     while True:
#         x = int(input("Number please - "))
#         if x == 0:
#             break
#         print(check(x))
# user()


# def cube(a):
#     return a**3
#
# def check_even(a):
#     while True:
#         if a % 2 == 0:
#             print(cube(a))
#             break
#         elif a!= 0:
#             print("odd number")
#             a = int(input("my number please - "))
#         elif a ==0:
#             break
#
# def user_2():
#     a = int(input("my number please - "))
#     check_even(a)
#
# user_2()

# def sum(a,b):
#     return a+b
#
# def user_two_numbers():
#     while True:
#         a = int(input("enter number a : - "))
#         b = int(input("enter number b : - "))
#         if sum(a,b) > 50:
#             print(sum(a,b))
#             print("Greater than 50")
#             break
#
#         elif sum(a,b) <50:
#             print("Less than 50")
#
#         a = int(input("enter number a : - "))
#         b = int(input("enter number b : - "))
#
# user_two_numbers()

for i in range(21):
    if i % 2 == 0:
        print(i)

for i in range(51):
    if i % 2 == 0:
        print(i)

for i in range(21):
    if i % 2 == 0:
        print(i,"even")
    if i%2!=0:
        print(i,"odd")

for i in range(1, 51):
    if i % 2 == 0 and i % 5 == 0:
        print(i)


count = 0
for i in range(1, 50):
    if i % 4 == 0:
        count += 1
print(count)

def square(n):
    return n ** 2
for n in range(1, 6):
    print(square(n))
print("----------------------")


def even(n):
    return n
for n in range(1,22):
    if even(n) % 2 == 0:
        print(even(n))

def even():
    for n in range(1,22):
         if n % 2 == 0:
            print(n)
even()

def returns():
    for i in range(-5,5):
        if i>0:
            print(i,"Positive")
        else:
            print(i,"Negative")
returns()

print("...................")

def cube():
    for n in range(1, 10):
        if n%2 ==0:
            print(n ** 3)
cube()

def odd_square():
    for i in range(1,10):
        if i % 2 ==1:
            print(i**2)
odd_square()

numbers = [1,2,4,5,7,9]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

x = [4,9,7,3,5,6]
x[3]= 100
print(x.append(55))
print(x.remove(7))
print(x.pop(0))
print(len(x))
if 9 in x:
    print("true")
print("--------------")

numbers = [12, 7, 24, 9, 30]
total = 0
for n in numbers:
    total = total + n

print(total)

numbers = [12, 7, 24, 9, 30]
count = 0
for n in numbers:
    if n % 2 == 0:
        count = count + 1

print(count)


numbers = [12, 7, 24, 9, 30]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)


nums = [100,1,7,58,6,93,2,4,57]
smaller = nums[0]
for i in nums:
    if i < smaller:
        smaller = i
print(smaller)
print("--------------------")

count = 0
evens = [4,7,8,9,6,2,1,5,6,12]
for i in evens:
    if i% 2 == 0:
        count = count + 1
print(count)

odds = [1,2,3,4,5,6,9,8,7]
empty = []
for i in odds:
    if i % 2 != 0:
        empty.append(i)
print(empty)


greats = [1,2,3,4,5,6,9,8,70]
count = 0
empty_great = []
for n in greats:
    if n > 20:
        empty_great.append(n)
        count += 1
print(empty_great)
print(count)

numbers = [12, 7, 24, 9, 30, 15, 8]
def evens():
    for i in numbers:
        if i % 2 == 0:
            print(i)
evens()


details = {
    "name" : "dinesh",
    "age" : 25,
    "place": "hyderabad"
}
for detail in details:
    print(detail, details[detail],sep = ", ")
print("-------------------------------")


nums = (12, 45, 8, 24, 67, 30, 11, 56)
def largest():
    larger = 0
    total = 0
    count = 0

    for n in nums:
        count = count + 1
        total = total + n

        if n > larger:
            larger = n
    print(larger)
    print(total)
    print(count)
largest()

numbers = (10, 20, 30, 20, 40, 50)
print(numbers[0])
if 40 in numbers:
    print("true")
print(numbers)

count = 0
for i in numbers:
    if  i == 20:
        count = count + 1
print(count)

print(numbers.index(50))

a,b,c = 10,20,30
print(a,b,c)

numbers = {10, 20, 30, 20, 10}
print(numbers)
print(numbers.discard(20))
print(numbers)

a = {10,20,5,40,9,15,4,6}
b = {7,8,9,4,5,6,3,12,1,0}
print(a|b)
print(a&b)
print(a-b)
print(a.add(99))
print(a.remove(9))
print(a)
if 40 in a:
    print("true")
students = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78,
    "Sneha": 95
}
print(students.keys())
# for student in students:
#     print(student)


students["kiran"] = 250
students["Rahul"] = 1000000
print(students)
del students["Arjun"]
print(students)

if "kiran" in students:
    print("true")

for student in students:
    print(student, students[student], sep=", ")

student_marks={
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78,
    "Sneha": 95
}

highest_marks = 0
highest_student = None
for details in student_marks:
    if student_marks[details]>highest_marks:
        highest_student = details
        highest_marks = student_marks[details]
print(highest_marks,highest_student)

student_marks = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78,
    "Sneha": 95
}
for details in student_marks:
    if student_marks[details] > 80:
        print(details, student_marks[details])


numbers = [12, 45, 8, 23, 56, 9, 34, 67, 20]
new_list = []
def is_even():
    for n in numbers:
        if n % 2 == 0:
            (new_list.append(n))
    print(new_list)
is_even()

even_list = set(new_list)
print(even_list)

squares = {}
for n in even_list:
    squares[n] = n**2
    print(n, squares[n])

# Final Practice: Easy → Hard

lists = [7,8,9,4,5,6,3,2,1]
new_list = []
def new():
    for n in lists:
        if n%2 == 0:
            new_list.append(n)
    print( new_list)
new()

new_set = set(new_list)
print(new_set)

def square(n):
    return n**2

new_dict = {}
for n in new_list:
    new_dict[n] = square(n)

print(new_dict)

lists = [7,8,9,4,5,6,3,2,1]
count = 0
total = 0
for n in lists:
    count = count + 1
    total = total + n
print(total)
print(count)

numbers = [12, 5, 27, 8, 19, 3]
def largest_number():
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n
            return largest

    # return largest

print(largest_number())

for i in range(1,4):
    for j in range(i):
        for x in range(i):
            print("*",end="")
        print()
    print()


def outer():
    def inner():
        print("Hello")

    inner()
outer()

numbers = [12, 5, 27, 8, 19, 3]
largest = numbers[0]
def larger_number():
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
            return largest
print(larger_number())


numbers = [12, 45, 8, 23, 56, 9, 34, 67, 20]
def even(n):
    return n % 2 == 0

new_list = []
count = 0
total = 0

for n in numbers:
    if even(n):
        new_list.append(n)
        count += 1
        total += n

print(new_list)
print(count)
print(total)

# try:
#     user = int(input("Enter a number: "))
#     print(10/user)
#
# except ValueError:
#     print("Enter valid number")
#
# except ZeroDivisionError:
#     print("cannot divide by zero")

# finally:
#     print("All done")  here it doesn't matter whether try and except valids finally will must print
# def main():
#     x = get_in()
#     return x
#
# def get_in():
#     try:
#          num = int(input("only Number: "))
#          print(num)
#
#     except ValueError:
#         print("enter a valid number")



# import mainn
# (mainn.is_even(87))


numbers = [10, 15, 20]
total = 0

for n in numbers:
    if n % 2 == 0:
        total = total + n
print(total)


#Its like creating the seperate dict and adding the greater value in that
student_marks = {
    "Rahul": 80,
    "Priya": 92,
    "Arjun": 75,
    "Sneha": 88
}
greater_85 = {}
for name, marks in student_marks.items():
    if marks > 85:
        greater_85[name] = marks
print(greater_85)

student_marks = {
    "Rahul": 80,
    "Priya": 92,
    "Arjun": 75,
    "Sneha": 88
}
student_marks["Rahul"]  = 101
print(student_marks)

class class_variable:
    school = "learning temple"

class instance_variable:
    def __init__(self, student):
        self.student = student

c1 = class_variable
print(c1.school)

s1 = instance_variable("nishithara")
print(s1.student)



from abc import ABC, abstractmethod

class Account(ABC):
    bank_name = "SBI"

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance    #encapsulation

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if self.is_valid_amount(amount):
            self.__balance += amount
        else:
            print("Amount must be positive")

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @abstractmethod
    def interest(self):
        pass

    def __str__(self):
        return f"{self.holder}: balance ₹{self.balance}"


class SavingsAccount(Account):
    def __init__(self, holder, balance, rate):
        super().__init__(holder, balance)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate / 100


class CurrentAccount(Account):
    def interest(self):
        return 0


class Bank:
    def __init__(self):
        self.accounts = []

    def open_savings(self, holder, balance, rate):
        account = SavingsAccount(holder, balance, rate)
        self.accounts.append(account)
        return account

    def open_current(self, holder, balance):
        account = CurrentAccount(holder, balance)
        self.accounts.append(account)
        return account

    def show_accounts(self):
        for account in self.accounts:
            print(account, "| interest:", account.interest())


bank = Bank()

a1 = bank.open_savings("Arjun", 10000, 5)
a2 = bank.open_current("Kiran", 8000)

a1.deposit(500)

bank.show_accounts()

print("Balance:", a1.balance)

Account.change_bank_name("HDFC")
print("Bank:", Account.bank_name)

