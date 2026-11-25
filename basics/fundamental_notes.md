**Functions And Variables...**

To print anything, we must use the inverted commas then only the code will execute correctly.

**print** is an built-in fuction which it takes arguments inside the paranthesis.

**Arguments** is nothing but which we wanted to deliver using the fuction/the imput which we are giving to the function.

**input** is a function which used for user interaction.

**variable** is used to store the value inside the computer variable is a container which it holds whatever num,string,img etc.

**Def func() return (5-8) call funs() print(func),**
here, 1.def func() first
and,  2.call func() second,takes the values if arguments there,
next, 3. inside the function takes the return value and sends to the computer memory deletes the def func() memory .
and, prints the value i.e call function.

Here difference between concatenation and comma seperator is seperates the items in the print function. and also concatenation does join  the items like one .

Now python is an in-built function which it has a parameters, **print("objects", "sep", end"/n")**
objects- Whatever we wanted to print, sep- Seperates the arguments, end"/n"- new line  -  here we can remove the /n, if we want the cursor to be in  the same line.

f-string - A string where you can directly insert variables or expressions inside {}...
ex- print("my name is" name,"Iam" age "years old")
it is not good to look at the code. instead we can use the fstring 

**print(f"my name is {name} iam {age} old) --- inside the bracers we can do expressions also**

print(f"my name is {name} iam {age+1} old)

**Python evaluates what's inside {}.**

f-string = normal text + {value} inserted wherever you want.

**String Methods**

There are many methods to do..

Capitalize- means the first letter of the sentence/word is capital

strip - means removes the white spaces from left and right not between ex- print("   dinesh nama   ")- 
output will be   hello dinesh  --- spaces over left and right

name = "   nama dinesh   "
print(name.strip().replace(" ","")) --- removes spaces right and left....replace helps to remove spaces in between
 The key difference between sep and replace is "sep" is it seperates or removes white spaces from the two arguments 
"replace" also removes the space but it can remove the space for single argument as well

basically in function to function or nested function 
"we need to question ourself whether who give the values "
means **user input- we dont need parameters cost()**
**but for function call we need parameters cost(price,quantity)**
**In Python, all non-default parameters must come first, and all default parameters must come at the very end.**
ex- def default(a=20.25,b):
    return a+b
print(default(1.8,4))

def default(a,b=7410):
    return a+b
print(default(1))

def default(a=20.25,b=87):
    return a+b
print(default())

def default(a=44,b=36):
    return a+b
print(default(1.8,4))

 **If you have a chain of three functions, you only need to call the very last function**
 # Function 1: The Basic Worker
def square(n):
    return n ** 2

# Function 2: The Middleman (Calls Function 1)
def double_the_square(n):
    return square(n) * 2

# Function 3: The Manager / Last Function (Calls Function 2)
def final_result(n):
    return double_the_square(n)

# --- THE MAIN SCRIPT ---
# You ONLY call the last function!
print(final_result(4))

**The main script is the unindented space at the bottom of your file where code executes automatically from top to bottom.**
**LOOP**
                        
while is a construct that asks me a question again and again
**while → runs until the condition becomes False. 🎯**

while condition:
    do something

loop stops when that condition becomes false.

**The easiest rule for choosing direction means when to use increment and decrement

Look at the condition.

If your condition looks like:
while i < 10:**

**A list is simply a way to store multiple values inside one variable.**

**Lists are mutable, meaning you can change their elements.**

**You can remove by value using "remove":**

**You can also remove by index using pop():**

**Checking whether something exists** (20 in numbers) this gives true/false.

**i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
i → index
numbers[i] → value**

**Most Important Operations**
numbers.append(50)
numbers.remove(20)
numbers.pop()
numbers.pop(2)
len(numbers)
20 in numbers
numbers[0]
numbers[-1]
numbers[1] = 100

i += 1  → move one step
count += 1 → found one more item
total += n → add the actual number
i += n → increase i by the value of n


Intersection means:
Give me the values that exist in BOTH sets.

Difference means:
Give me the values that are in the first set but NOT in the second set

**NESTED LOOPS**
outer loop runs once
    ↓
inner loop runs completely
    ↓
outer loop moves to next value
    ↓
inner loop runs completely again

numbers = [12, 5, 27, 8, 19, 3]

def largest_number(numbers):
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n

    return largest
print(largest_number(numbers))

students = {
    "Rahul": 85,
    "Priya": 92,
    "Arjun": 78,
    "Sneha": 95
}

for name, marks in students.items():
    print(name, marks)

**Write one program that:**

uses a function to check even numbers
uses for
creates a new list containing the even numbers
finds the count and sum of those even numbers
prints the final list, count, and sum.

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

**Exceptions
An exception is an error that happens while the program is running and interrupts normal execution**.
using try
  ↓
code runs
  ↓
if thats error?
 ┌───────┐
 yes     no
 ↓       ↓
except   continue

ValueError         → value can't be converted/used as required
ZeroDivisionError  → division by zero
NameError          → variable/name doesn't exist

**Debugging..**
Error message → line number → understand the problem → fix → run again

if __name__ == "__main__":
This trick is incredibly useful in Python because it allows you to write test code or
execution scripts inside a file without worrying about it accidentally running or messing up your logic when you import its functions elsewhere

Imagine we have a student data like his..
name = rahul
marks = 89
In seperate blocks..... and if i have more data i need to write same this seperately.
    it's a very tough job to do. 
imagine if we create a seperate databox for entire details of that person that databox is known as object

A class variable is shared by every object in the class,
while an instance variable belongs only to one specific object.

Abstraction is the tool used to enforce rules and standards across your code.

The Difference in One Sentence:

• Normal Inheritance: The child inherits everything from the parent, but can choose to change things or leave them alone.
• Abstraction (Strict Inheritance): The child inherits from the parent, but the parent forces a rule saying, 
"You must rewrite this specific method or I won't let you run."

@property decorator is for not using paranthesis for method.but class must

Transforming every item in the list we use map
result = list(map(lambda x:x**2 , employees))

quick remainder:
if a list demanding the highest earner we do compararision method(single person)
if a list demanding the higher earners(multiple people) we do append.
