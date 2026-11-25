import csv


with open("employees_practice.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    #All the department names will be printed
    # for row in reader:
    #     print(row)

#If you wanna call individual records
    next(reader)  # Skip header
    for number, row in enumerate(reader, start=1):
        if number == 3:
            print(row)
            break

#Dictreader means all the records will print in dict form

with open("employees_practice.csv","r",newline="", encoding="utf-8") as file:
    Dictreader = csv.DictReader(file)
    for row in Dictreader:
        # print(row["name"],row["department"])
        print(row)

    Dickreader = csv.DictReader(file)
    file.seek(0)  #this helps that again go back to the start and again begin the loop

    for number,row in enumerate(Dictreader, start=1):
        if number == 6:
            print(row)
            break