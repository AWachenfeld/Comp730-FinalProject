import os
import sys
from telecom_translate import Subscriptions
from telecom_translate import Contractrenewal
from telecom_translate import Monthlycharges
from telecom_translate import Tenure

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

def telecom_main():
    print(f"""\nChoose what Telecom user data you would like to see:
    1: Subscriptions owned by users
    2: Contract renewals
    3: Monthly charges avg
    4: Tenure avg (months)
    5: Exit Program""")
    telecom_choice = input("Enter num choice: ")

    if (telecom_choice == "1"):
        print(f"""What subscription amount would you like to see:
        1: 3 Subscriptions Owned
        2: 2 Subscriptions Owned
        3: 1 Subscriptions Owned""")
        subscription_choice = input("Enter choice: ")
        if (subscription_choice == "1"):
            subscriptions_owned(subscription_choice)
        elif (subscription_choice == "2"):
            subscriptions_owned(subscription_choice)
        elif (subscription_choice == "3"):
            subscriptions_owned(subscription_choice)
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            telecom_main()

    elif (telecom_choice == "2"):
        print(f"""Would you like to see contract renewals for seniors or non-seniors?:
        1: Seniors
        2: non-Seniors""")
        renewal_choice = input("Enter choice: ")
        if (renewal_choice == "1"):
            contract_renewal(renewal_choice)
        elif (renewal_choice == "2"):
            contract_renewal(renewal_choice)
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            telecom_main()

    elif (telecom_choice == "3"):
        monthly_charges()
        telecom_main()

    elif (telecom_choice == "4"):
        tenure_avg()
        telecom_main()

    elif (telecom_choice == "5"):
        print("Thank You, Goodbye!")
        sys.exit()
    else:
        print("You choice was not valid. Please select from the list.\n")
        telecom_main()


def subscriptions_owned(choice):
    input1 = '../data/telecom_users.txt'
    devs_obj = Subscriptions(input1)
    result = devs_obj.subscriptions_owned()
    if (choice == "1"):
        print(f"""\n{result["3_owned"]} Users own 3 subscriptions.\n""")
    elif (choice == "2"):
        print(f"""\n{result["2_owned"]} Users own 2 subscriptions.\n""")
    elif (choice == "3"):
        print(f"""\n{result["1_owned"]} Users own only 1 subscription.\n""")


def contract_renewal(choice):
    input1 = '../data/telecom_users.txt'
    devs_obj = Contractrenewal(input1)
    result = devs_obj.contract_renewal()
    if (choice == "1"):
        print(f"""\n{result["Senior_renew"]} Seniors will renew their contract,""")
        print(f"""{result["Senior_cancel"]} senior will cancel their contract.\n""")
    elif (choice == "2"):
        print(f"""\n{result["NonSenior_renew"]} NonSeniors will renew their contract,""")
        print(f"""{result["NonSenior_cancel"]} Nonsenior will cancel their contract.\n""")

def monthly_charges():
    input1 = '../data/telecom_users.txt'
    devs_obj = Monthlycharges(input1)
    result = devs_obj.monthly_charges()
    print(f"""\nFor {result["Senior_total"]} Seniors their avg monthly charges are ${result["Senior_charges"]},""")
    print(f"""For {result["NonSenior_total"]} NonSeniors their avg monthly charges are ${result["NonSenior_charges"]}.\n""")

def tenure_avg():
    input1 = '../data/telecom_users.txt'
    devs_obj = Tenure(input1)
    result = devs_obj.tenure_avg()
    print(f"""\nBased on {result["Senior_total"]} Seniors their avg teunre is {result["Senior_months"]} months,""")
    print(f"""Based on {result["NonSenior_total"]} NonSeniors their avg tenure is {result["NonSenior_months"]} months.\n""")
