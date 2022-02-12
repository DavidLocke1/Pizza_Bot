import random
from random import randint

# list of random names
names = ["Mark", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Eris", "Moana", "Lewis", "Lara"]

def welcome():
    """
    Purpose: To genertate a random name from the list and print out a 
    welcome message
    Paramaters: None
    Returns: None
    """
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to dream pizza ***")
    print("*** My name is ",name," ***")
    print("*** I will be here to help you order your delicious Dream Pizza ***")

def main():
    """
    Purpose: To run all functions
    Parameters: None
    Returns: None
    """
    welcome()

main()