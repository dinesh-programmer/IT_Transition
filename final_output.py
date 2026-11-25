# Iam gonna do employee data problem covering all the pieces which i've learned so far
from wsgiref.simple_server import software_version

employees = [
    {"name":"Dinesh","salary":150000},
    {"name":"Arjun","salary":89000},
    {"name": "Priya", "salary": 60000},
    {"name": "Kiran", "salary": 35000}
]
#Write a function that does three things:
# Accepts the employee list and a minimum salary.
# Keeps only employees whose salary is at least ₹30,000, retaining both their names and salaries.
# Sorts those employees from highest salary to lowest.


def min_salary(employees):
    filtered_salary = employees[0]
    for i in employees:
        if i["salary"] < filtered_salary["salary"]:
            filtered_salary= i
    return filtered_salary

result = min_salary(employees)
print(result)

def least_salary(employees):
    filtered_salary = employees[0]
    for i in employees:
        if i["salary"] < 60000:
            filtered_salary = i
    return filtered_salary

result = least_salary(employees)
print(result)

def find_high_salary(employees):
    compared_salary = employees[0]
    for i in employees:
        if i["salary"] > compared_salary["salary"]:
            compared_salary = i
    return compared_salary
result = find_high_salary(employees)
print(result)

def find_high_earners(employees):
    high_earners = []
    for i in employees:
        if i["salary"] > 40000:
            high_earners.append(i)
    return high_earners
result = find_high_earners(employees)
print(result)

def count_numbers(employees):
    count = 0
    for i in employees:
        if i["salary"] < 40000:
            count = count + 1
    return count
result = count_numbers(employees)
print(result)

def sorts(employees):
    sorting  = sorted(employees, key=lambda x:x["salary"],reverse = True)
    return sorting
result = sorts(employees)
print(result)

#Indexing: word[0]
# Slicing: word[1:4]
# Length: len(word)
# Membership: "a" in word
# Case conversion: upper(), lower()
# Splitting: split()
# Replacing: replace()

x = "membership"
# res = x[5:8] --rsh
res = x[:2]
print(res)

text = "python programming"
print(text[::-2])

#Python always goes forward by default it adds +1.
#It expects the start index should be less than the endone
#Because when (3:2).it won't print unless the step in negative

tasks = " software "
# print(tasks.isupper())  #bool
# print(tasks.replace(" ","")) #soft ware (removes the gap bet them)
print(tasks.strip(" ")) # removes the gap at edges
print(tasks.replace("soft", "hard").strip())

sentence = ["yoo", "buddy", "whats", "the", "matter"]
# print(sentence.split())
res = print(" ".join(sentence)) #syntax for joining

x = "dineshh"
print(x.count("h"))
print(x.find("a"))
# print(x.index("a"))#Both index and find helps for finding the number.but if the value is not found then
                    # it throws error for the index not find.

print("ne" in x)  #Check whether a word exists inside a sentence.

# Check whether a string contains only digits or only alphabetic characters.
code1 = "123454"
code2 = "dinesh"
print(code1.isalpha())
print(code2.isdigit())

sequence = "Dinesh ela unav Ro"
# consonants = "abcdefghijkl"
upper_count = 0
lower_count = 0
for i in sequence:
    if i.isupper():
        upper_count = upper_count + 1
    elif i.islower():
        lower_count = lower_count + 1
print(upper_count, lower_count)


# Build a new string containing only the vowels.

x = "hello dinesh"
y = "aeimnouph"
vowels  = "AEIOUUaeiou"
new_str =""
for i in x:
    if i in vowels:
        new_str = new_str + i

import re
removing = "namadinesh@123"
# If you want to delete or remove the digits,
# you have to replace them with nothing, which is represented by an empty string ('').

res = re.sub(r'\d','',removing)
print(res)

items1 = [1,2,3,3,4,5,5,6,6,7,78]
items2 = [9,8,7,4,45,6,3,2,1]


def calculate_bonus(salary, bonus_rate=10):
    bonus = salary * bonus_rate/100
    return bonus

print(calculate_bonus(50000,2))
print(calculate_bonus(300))

dick = {
    "name" : "dinesh",
    "age" : 24,
    "city": "hyderabad"
}
print(dick["name"])

for i in dick:
    if i[1] == "dinesh":
        print(i[1])
employees = [
    {"name": "Ravi", "salary": 30000},
    {"name": "Arun", "salary": 50000},
    {"name": "Amit", "salary": 40000}
]

