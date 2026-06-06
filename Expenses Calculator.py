# Expenses Calculator
from tabulate import tabulate
import csv
import os
path = os.path.join(os.path.dirname(__file__), "Products.csv")

def Product_Input():
    while True:
        Product_Name = str(input("Input product name : "))
        while True:
            try:
                Product_Price = float(input("Input product price : $"))
                break
            except ValueError:
                print("Input a number!")

        while True:
            Product_Duration = (input("Input product payment period (Once, Daily, Weekly, Monthly, Yearly) : "))
            if Product_Duration.lower() not in ["once", "daily", "weekly", "monthly", "yearly"]:
                print("Try again")
            else:
                Product_Duration = Product_Duration.capitalize()
                break
        
        file_empty = not os.path.exists(path) or os.path.getsize(path) == 0

        with open(path, "a", newline="") as Input_Products:
            Fields = ["Product Name", "Product Price", "Product Payment Period"]
            write = csv.DictWriter(Input_Products, fieldnames=Fields)
            if file_empty:
                write.writeheader()
            write.writerow({"Product Name" : Product_Name, "Product Price" : Product_Price, "Product Payment Period" : Product_Duration})

        while True:
            Loop = str(input("Would you like to input again? (Y/N) : "))
            if Loop.lower() == "y":
                break
            elif Loop.lower() == "n":
                return
            else:
                print("Try again")
        
def Product_And_Price():
    if not os.path.exists(path):
        print("There's nothing to show!")
        return
    Products_List = []
    with open(path, "r") as Products_Info:
        read = csv.DictReader(Products_Info)
        for Products in read:
           Products_List.append(Products)
    if not Products_List:
        print("There's nothing to show!")
    else:
        print(tabulate(Products_List, headers="keys", tablefmt="grid"))

def Product_Total_Price():
    Total = 0
    if not os.path.exists(path):
        print("There's nothing to show!")
        return
    Products_List = []
    with open(path, "r") as Products_Info:
        read = csv.DictReader(Products_Info)
        for product in read:
            Products_List.append(product)

    for products in Products_List:
        daily_payment = 0
        if products["Product Payment Period"].lower() == "once":
            continue
        elif products["Product Payment Period"].lower() == "daily":
            daily_payment = float(products["Product Price"])
        elif products["Product Payment Period"].lower() == "weekly":
            daily_payment = float(products["Product Price"]) / 7
        elif products["Product Payment Period"].lower() == "monthly":
            daily_payment = float(products["Product Price"]) / 30
        elif products["Product Payment Period"].lower() == "yearly":
            daily_payment = float(products["Product Price"]) / 365
        Total += daily_payment
    return Total
    
def Expenses_Duration(Total):
    while True:
            Duration = input("Enter calculation period (Daily, Weekly, Monthly, Yearly) : ")
            if Duration.lower() == "daily" or Duration.lower() == "day":
                multiplier = 1
                break
            elif Duration.lower() == "weekly" or Duration.lower() == 'week':
                multiplier = 7
                break
            elif Duration.lower() == "monthly" or Duration.lower() == 'month':
                multiplier = 30
                break
            elif Duration.lower() == "yearly" or Duration.lower() =='year':
                multiplier = 365
                break
            else:
                print("Try again")

    Calculated_Data = []
    if not os.path.exists(path):
        print("There's nothing to show!")
        return
    Products_List = []
    with open(path, "r") as Products_Info:
        read = csv.DictReader(Products_Info)
        for product in read:
            Products_List.append(product)

    for products in Products_List:
        daily_payment = 0
        if  products["Product Payment Period"].lower() == "once":
            Calculated_Data.append({"Product Name" : products["Product Name"], "Total Price" : "$" + str(round(float(products["Product Price"])))})
            continue
        elif products["Product Payment Period"].lower() == "daily":
            daily_payment = float(products["Product Price"])
        elif products["Product Payment Period"].lower() == "weekly":
            daily_payment = float(products["Product Price"]) / 7
        elif products["Product Payment Period"].lower() == "monthly":
            daily_payment = float(products["Product Price"]) / 30
        elif products["Product Payment Period"].lower() == "yearly":
            daily_payment = float(products["Product Price"]) / 365
        Calculated_Data.append({"Product Name" : products["Product Name"], "Total Price" : "$" + str(round(daily_payment * multiplier, 2))})

    print(tabulate(Calculated_Data, headers="keys", tablefmt="grid"))
    Once_total = 0
    for p in Products_List:
        if p["Product Payment Period"].lower() == "once":
            Once_total += float(p["Product Price"])
    print("Your total expenses : $" + str(round(Total * multiplier + Once_total)))

def Remove_Products():
    if not os.path.exists(path):
        print("There's nothing to show!")
        return
    New_Products_List = []
    with open(path, "r") as Product_Info:
        read = csv.DictReader(Product_Info)
        for index, product in enumerate(read):
            print(f"{index + 1}. {product['Product Name']} - ${product['Product Price']} - {product["Product Payment Period"]}")
            New_Products_List.append(product)
    
    while True:
        try:
            Remove = int(input("Select product number to remove : "))
            if 1 <= Remove <= len(New_Products_List):
                break
            else:
                print(f"Input a number between 1 and {len(New_Products_List)}")
        except ValueError:
            print("Input a number!")
    
    New_Products_List.pop(Remove - 1)

    with open(path, "w", newline="") as Output_File:
        fields = ["Product Name", "Product Price", "Product Payment Period"]
        write = csv.DictWriter(Output_File, fieldnames=fields)
        write.writeheader()
        write.writerows(New_Products_List)

def Change_Price():
    if not os.path.exists(path):
        print("There's nothing to show!")
        return
    New_Products_List = []
    with open(path, "r") as Product_Info:
        read = csv.DictReader(Product_Info)
        for index, product in enumerate(read):
            print(f"{index + 1}. {product['Product Name']} - ${product["Product Price"]}")
            New_Products_List.append(product)
    while True:
        try:
            Change = int(input("Select product number to change price : "))
            if 1 <= Change <= len(New_Products_List):
                break
            else:
                print(f"Input a number between 1 and {len(New_Products_List)}")
        except ValueError:
            print("Input a number!")

    while True:
        try:
            New_Price = float(input("Input new price : $"))
            break
        except ValueError:
            print("Input a number!")

    New_Products_List[Change - 1]["Product Price"] = New_Price

    with open(path, "w", newline="") as Output_File:
        fields = ["Product Name", "Product Price", "Product Payment Period"]
        write = csv.DictWriter(Output_File, fieldnames=fields)
        write.writeheader()
        write.writerows(New_Products_List)

def Change_Expense_Period():
    if not os.path.exists(path):
        print("There's nothing to show!")
        return
    New_Products_List = []
    with open(path, "r") as Product_Info:
        read = csv.DictReader(Product_Info)
        for index, product in enumerate(read):
            print(f"{index + 1}. {product["Product Name"]} - ${product["Product Payment Period"]}")
            New_Products_List.append(product)
    while True:
        try:
            Change_Period = int(input("Select product number to change expense period : "))
            if 1 <= Change_Period <= len(New_Products_List):
                break
            else:
                print(f"Input a number between 1 and {len(New_Products_List)}")
        except ValueError:
            print("Input a number!")

    while True:
        New_Period = input("Input new expense period (Once, Daily, Weekly, Monthly, Yearly) : ")
        if New_Period.lower() not in ["once", "daily", "weekly", "monthly", "yearly"]:
            print("Try again")
        else:
            break

    New_Products_List[Change_Period - 1]["Product Payment Period"] = New_Period.capitalize()    

    with open(path, "w", newline="") as Output_File:
        fields = ["Product Name", "Product Price", "Product Payment Period"]
        write = csv.DictWriter(Output_File, fieldnames=fields)
        write.writeheader()
        write.writerows(New_Products_List)

while True:
    Features = input("What Would You Like To Do? (Add Product, Remove Product, Show Products, Change Price, Change Expense Period, Calculate Total Expenses, Quit) : ")
    if Features.lower() == "add product" or Features.lower() == "add":
        Product_Input()
    elif Features.lower() == "remove product" or Features.lower() == "remove":
        Remove_Products()
    elif Features.lower() == "show products" or Features.lower() == "show":
        Product_And_Price()
    elif Features.lower() == "change price":
        Change_Price()
    elif Features.lower() == 'change expense period' or Features.lower() == "change expense":
        Change_Expense_Period()
    elif Features.lower() == "calculate total expenses" or Features.lower() == "calculate":
        Total = Product_Total_Price()
        if Total is not None:
            Expenses_Duration(Total)
    elif Features.lower() == "quit":
        print("Thanks for calculating, byebye!")
        break
    else:
        print("Try again")