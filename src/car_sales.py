import pandas as pd
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)



import pandas as pd

df = pd.read_csv('../data/car_sales.csv')
pd.set_option('display.max_columns', 500)



def car_main():
    print("Choose car option")
    print(f"""    1. Select by manufacturer
    2. Sales
    3. Fuel Capacity
    4. Fuel Efficiency
    5. Horsepower""")

    choice = input("Choose car option: ")

    if(choice == "1"):
        select_by_manufacturer()
    elif(choice == "2"):
        sales_in_thousands()
    elif(choice == "3"):
        fuel_capacity()
    elif(choice == "4"):
        fuel_efficiency()
    elif(choice == "5"):
        horsepower()
    else:
        print(choice)

def select_by_manufacturer():
    print(f""" Select a manufacturer:
    Acura, Audi, BMW, Buick, Cadillac, Chevrolet, Chrysler, Dodge, Ford, Honda,
    Hyundai, Infiniti, Jaguar, Jeep, Lexus, Lincoln, Mitsubishi, Mercury, 
    Mercedes-B, Nissan, Oldsmobile, Plymouth, Pontiac, Porsche, Saab, Saturn, Subaru, 
    Toyota, Volkswagen, Volvo""")
    man = input("Select Manufacturer: ")

    man_valid = False
    manufacturers = ['ACURA', 'AUDI', 'BMW', 'BUICK', 'CADILLAC', 'CHEVROLET', 'CHRYSLER', 'DODGE', 'FORD', 'HONDA', 'HYUNDAI', 'INFINITI', 'JAGUAR', 'JEEP', 'LEXUS', 'LINCOLN', 'MITSUBISHI', 'MERCURY', 'MERCEDES-B', 'NISSA', 'OOLDSMOBILE', 'PLYMOUTH', 'PONTIAC', 'PORSCHE', 'SAAB', 'SATURN', 'SUBARU', 'TOYOTA', 'VOLKSWAGEN', 'VOLVO']

    for i in  range(len(manufacturers)):
        if (manufacturers[i] == man.upper()):
            man_valid = True
            print(df.loc[df['Manufacturer'] == man.upper()])
            break
            
    if(man_valid == False):
        print("Invalid manufacturer choice")
        select_by_manufacturer()

def sales_in_thousands():
    print(f"""\n Choose cars based off their sale price:
    1. Under $10k
    2. $10k - $15k
    3. $15k - $20k
    4. Greater than $20k""")
    amount = input("Select option: ")

    if(amount == "1"):
        less = df.loc[df['Sales_in_thousands'] < 10]
        print(less.head(50))
    elif(amount == "2"):
        most = df.loc[df['Sales_in_thousands'] >= 10]
        mosta = most.loc[most['Sales_in_thousands'] < 15]
        print(mosta.head(50))
    elif(amount == "3"):
        many = df.loc[df['Sales_in_thousands'] >= 15]
        manya = many.loc[many['Sales_in_thousands'] < 20]
        print(manya.head(50))
    elif(amount == "4"):
        highest = df.loc[df['Sales_in_thousands'] >= 20]
        print(highest.head(50))
    else:
        print("Invalid option please choose an option listed above")
        sales_in_thousands()

def fuel_capacity():
    print(f"""\n Choose cars based off their fuel capacity:
    1. Less than 15 gallons
    2. 15 - 25 gallons
    3. Greater than 25 gallons""")
    capac = input("Select option: ")

    if(capac == "1"):
        less = df.loc[df['Fuel_capacity'] < 15]
        print(less.head(50))
    elif(capac == "2"):
        most = df.loc[df['Fuel_capacity'] >= 15]
        mosta = most.loc[most['Fuel_capacity'] < 25]
        print(mosta.head(50))
    elif(capac == "3"):
        many = df.loc[df['Fuel_capacity'] >= 25]
        print(many.head(50))
    else:
        print("Invalid option please choose an option listed above")
        fuel_capacity()

def fuel_efficiency():
    print(f"""\n Choose cars based off their fuel efficiency:
    1. Less than 18 mpg
    2. 18 - 28 mpg
    3. Greater than 28 mpg""")
    eff = input("Select option: ")

    if(eff == "1"):
        less = df.loc[df['Fuel_efficiency'] < 18]
        print(less.head(50))
    elif(eff == "2"):
        most = df.loc[df['Fuel_efficiency'] >= 18]
        mosta = most.loc[most['Fuel_efficiency'] < 28]
        print(mosta.head(50))
    elif(eff == "3"):
        many = df.loc[df['Fuel_efficiency'] >= 28]
        print(many.head(50))
    else:
        print("Invalid option please choose an option listed above")
        fuel_efficiency()

def horsepower():
    print(f"""\n Choose cars based off their horsepower:
    1. Under 100
    2. 100 - 200
    3. 200 - 300
    4. Greater than 300""")
    horse = input("Select option: ")

    if(horse == "1"):
        less = df.loc[df['Horsepower'] < 100]
        print(less.head(50))
    elif(horse == "2"):
        most = df.loc[df['Horsepower'] >= 100]
        mosta = most.loc[most['Horsepower'] < 200]
        print(mosta.head(50))
    elif(horse == "3"):
        many = df.loc[df['Horsepower'] >= 200]
        manya = many.loc[many['Horsepower'] < 300]
        print(manya.head(50))
    elif(horse == "4"):
        highest = df.loc[df['Horsepower'] >= 300]
        print(highest.head(50))
    else:
        print("Invalid option please choose an option listed above")
        horsepower()