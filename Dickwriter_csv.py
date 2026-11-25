import csv
#It's just creating the csv records..
with open("employees_dictwriter.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(    #writer is variable, disctwriter is in dict format
        file,
        fieldnames=["ID", "Name", "Department"]
    )

    writer.writeheader() #This line is for column names
    writer.writerows([  #writerows is for adding rows(muultiple)
        {"ID": 101, "Name": "Ravi", "Department": "IT"},
        {"ID": 102, "Name": "Arun", "Department": "HR"},
        {"ID": 103, "Name": "Sneha", "Department": "Finance"}
    ])

print("File created successfully")

# Now try to append some records, same like writing only.
with open("employees_dictwriter.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["ID", "Name", "Department"]
    )
    writer.writerows([
        {"ID": 104, "Name": "Suneeth", "Department": "Sales"}
    ])

with open("employees_dictwriter.csv","r",newline="",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

import csv

# Read existing records
with open("employees_practice.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# 1. FILTER: Employees earning 40000 or more
for row in employees:
    if int(row["salary"]) >= 40000:
        print(row["name"], row["salary"])


# 2. UPDATE: Change Ravi's salary
for row in employees:
    if row["employee_id"] == "101":
        row["salary"] = "45000"


# 3. DELETE: Remove employee 102
employees = [
    row for row in employees
    if row["employee_id"] != "102"
]

# Save modified records into a new CSV
with open("employees_updated.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()
    writer.writerows(employees)

print("Updated successfully")
