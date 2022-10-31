import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


def main():
    choice = input("Enter username: ")
    print("Username is: " + choice)

if __name__ == '__main__':
    main()
