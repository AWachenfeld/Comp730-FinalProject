import os
import sys
from telecom_main import telecom_main

#from cars_main import cars_main
#from fantasy_main import fantasy_main

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


def main():
    print(f"""Based on avaiable dataset please choose from the available list:
    1: Telecom Users
    2:
    3: Car Sales
    4: Fantasy Football
    5: Exit Program""")
    choice = input("Choose a number: ")
    if (choice == "1"):
        telecom_main()
    #elif (choice == "2"):

    #elif (choice == "3"):
        #cars_main()
    #elif (choice == "4"):
        #fantasy_main()
    elif (choice == "5"):
        print("Thank You, Goodbye!")
        sys.exit()
    else:
        print("You choice was not valid. Exiting Process.")
        sys.exit()
    print("Would you like to choose a new dataset?")
    choice_continue = input("(Y/N): ")
    if (choice_continue.upper() == "Y"):
        main()
    else:
        print("Thank You, Goodbye!")
        sys.exit()

if __name__ == '__main__':
    main()
