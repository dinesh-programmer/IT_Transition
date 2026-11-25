import json

with open("employees.json","r",encoding="utf-8") as file:
    data = json.load(file)
    # print(data)
    # print(data[0]["name"])  #ravi
    for employee in data:
        # print(employee["name"]) #prints every employee name
        print(employee)

        if employee["employee_id"] == 101:
            employee["salary"] = 75000
            print(employee)

    #Checking wheather the data modified..
    #Changed but only in python's memory not in actual json file..
    print(data)

#This changes the original file and permanently saves in json file..
# Use json.dumps() when you want the updated data as a JSON string:

with open("employees.json","w",encoding="utf-8") as file:
    json.dump(data,file,indent=4)

