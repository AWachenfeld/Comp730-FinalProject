import os
import sys
from telecom_translate import Subscriptions
from telecom_translate import Contractrenewal

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
)

def telecom_main():
    print("You chose Telecom user data")
    print(f"""Choose what you would like to see:
    1: Subscriptions owned by users
    2: Contract renewals
    3: Exit Program""")
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
        if (subscription_choice == "1"):
            contract_renewal(renewal_choice)
        elif (subscription_choice == "2"):
            contract_renewal(renewal_choice)
        else:
            print("You choice was not valid. Returning to Telecom options menu.\n")
            telecom_main()
    elif (telecom_choice == "3"):
        print("Thank You, Goodbye!")
        exit()
    else:
        print("You choice was not valid. Please select from the list.\n")
        telecom_main()


def subscriptions_owned(choice):
    input1 = './data/telecom_users.txt'
    devs_obj = Subscriptions(input1)
    result = devs_obj.subscriptions_owned()
    if (choice == "1"):
        print(f"""{result["3_owned"]} Users own 3 subscriptions.\n""")
    elif (choice == "2"):
        print(f"""{result["2_owned"]} Users own 2 subscriptions.\n""")
    elif (choice == "3"):
        print(f"""{result["1_owned"]} Users own only 1 subscription.\n""")


def contract_renewal():
    input1 = './data/telecom_users.txt'
    devs_obj = Contractrenewal(input1)
    result = devs_obj.contract_renewal()
    print(f"""Based on a users seniority these are the renewals and cancelations!
    {result["Senior_renew"]} Seniors will renew their contract,
    {result["Senior_cancel"]} senior will cancel their contract,
    {result["NonSenior_renew"]} Nonseniors will renew their contract, and
    {result["NonSenior_cancel"]} Nonseniors will cancel their contract.\n""")
