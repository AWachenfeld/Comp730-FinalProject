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
    2: Contract renewals""")
    telecom_choice = input("Enter num choice: ")
    if (telecom_choice == "1"):
        subscriptions_owned()
    elif (telecom_choice == "2"):
        contract_renewal()
    else:
        print("You choice was not valid. Please select from the list.\n")
        telecom_main()


def subscriptions_owned():
    input1 = './data/telecom_users.txt'
    devs_obj = Subscriptions(input1)
    result = devs_obj.subscriptions_owned()
    print(f"""The number of subscriptions owned users are!
    {result["3_owned"]} Users own 3 subscriptions,
    {result["2_owned"]} Users own 2 subscriptions, and
    {result["1_owned"]} Users own only 1 subscription.\n""")
