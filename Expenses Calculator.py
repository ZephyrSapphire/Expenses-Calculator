# Expenses Calculator
from tabulate import tabulate
Products_List = []

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
                break
        
        Products_List.append({"Product Name" : Product_Name, "Product Price" : Product_Price, "Product Payment Period" : Product_Duration})
        while True:
            Loop = str(input("Would you like to input again? (Y/N) : "))
            if Loop.lower() == "y":
                break
            elif Loop.lower() == "n":
                return
            else:
                print("Try again")
        
def Product_And_Price():
        print(tabulate(Products_List, headers="keys", tablefmt="grid"))

def Product_Total_Price():
    Total = 0
    for products in Products_List:
        daily_payment = 0
        if products["Product Payment Period"].lower() == "once":
            continue
        elif products["Product Payment Period"].lower() == "daily":
            daily_payment = products["Product Price"]
        elif products["Product Payment Period"].lower() == "weekly":
            daily_payment = products["Product Price"] / 7
        elif products["Product Payment Period"].lower() == "monthly":
            daily_payment = products["Product Price"] / 30
        elif products["Product Payment Period"].lower() == "yearly":
            daily_payment = products["Product Price"] / 365
        Total += daily_payment
    return Total
    
def Expenses_Duration(Total):
    while True:
            Duration = input("Enter calculation period (Daily, Weekly, Monthly, Yearly) : ")
            if Duration.lower() == "daily":
                multiplier = 1
                break
            elif Duration.lower() == "weekly":
                multiplier = 7
                break
            elif Duration.lower() == "monthly":
                multiplier = 30
                break
            elif Duration.lower() == "yearly":
                multiplier = 365
                break
            else:
                print("Try again")

    Calculated_Data = []
    for products in Products_List:
        daily_payment = 0
        if  products["Product Payment Period"].lower() == "once":
            Calculated_Data.append({"Product Name" : products["Product Name"], "Total Price" : "$" + str(round(products["Product Price"]))})
            continue
        elif products["Product Payment Period"].lower() == "daily":
            daily_payment = products["Product Price"]
        elif products["Product Payment Period"].lower() == "weekly":
            daily_payment = products["Product Price"] / 7
        elif products["Product Payment Period"].lower() == "monthly":
            daily_payment = products["Product Price"] / 30
        elif products["Product Payment Period"].lower() == "yearly":
            daily_payment = products["Product Price"] / 365
        Calculated_Data.append({"Product Name" : products["Product Name"], "Total Price" : "$" + str(round(daily_payment * multiplier, 2))})

    print(tabulate(Calculated_Data, headers="keys", tablefmt="grid"))
    Once_total = 0
    for p in Products_List:
        if p["Product Payment Period"].lower() == "once":
            Once_total += p["Product Price"]
    print("Your total expenses : $" + str(round(Total * multiplier + Once_total)))

def Remove_Products(Products_List):
    for index, product in enumerate(Products_List):
        print(f"{index + 1}. {product['Product Name']} - ${product["Product Price"]}")
    while True:
        try:
            Remove = int(input("Select product number to remove : "))
            if 1 <= Remove <= len(Products_List):
                break
            else:
                print(f"Input a number between 1 and {len(Products_List)}")
        except ValueError:
            print("Input a number!")
    
    Products_List.pop(Remove - 1)
    return Remove

def Change_Price(Products_List):
    for index, product in enumerate(Products_List):
        print(f"{index + 1}. {product['Product Name']} - ${product["Product Price"]}")
    while True:
        try:
            Change = int(input("Select product number to change price : "))
            if 1 <= Change <= len(Products_List):
                break
            else:
                print(f"Input a number between 1 and {len(Products_List)}")
        except ValueError:
            print("Input a number!")

    while True:
        try:
            New_Price = float(input("Input new price : $"))
            break
        except ValueError:
            print("Input a number!")

    Products_List[Change - 1]["Product Price"] = New_Price

def Change_Expense_Period(Products_List):
    for index, product in enumerate(Products_List):
        print(f"{index + 1}. {product["Product Name"]} - ${product["Product Price"]}")
    while True:
        try:
            Change_Period = int(input("Select product number to change expense period : "))
            if 1 <= Change_Period <= len(Products_List):
                break
            else:
                print(f"Input a number between 1 and {len(Products_List)}")
        except ValueError:
            print("Input a number!")

    while True:
        New_Period = input("Input new expense period (Once, Daily, Weekly, Monthly, Yearly) : ")
        if New_Period.lower() not in ["once", "daily", "weekly", "monthly", "yearly"]:
            print("Try again")
        else:
            break

    Products_List[Change_Period - 1]["Product Payment Period"] = New_Period.lower()

Product_Input()

while True:
    Features = input("What Would You Like To Do? (Add Product, Remove Product, Show Products, Change Price, Change Expense Period, Calculate Total Expenses, Quit) : ")
    if Features.lower() == "add product":
        Product_Input()
    elif Features.lower() == "remove product":
        Remove_Products(Products_List)
    elif Features.lower() == "show products":
        Product_And_Price()
    elif Features.lower() == "change price":
        Change_Price(Products_List)
    elif Features.lower() == 'change expense period':
        Change_Expense_Period(Products_List)
    elif Features.lower() == "calculate total expenses":
        Total = Product_Total_Price()
        Expenses_Duration(Total)
    elif Features.lower() == "quit":
        print("Thank's for calculating, ByeBye!")
        break
    else:
        print("Try again")
