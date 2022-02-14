# pizza bot program
import random
from random import randint

# list of random names
names = ["Mark", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Eris", "Moana", "Lewis", "Lara"]


# welcome message with random name
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


# menu for pick-up or delivery

def pickup():
    print("Is your order for pickup or delivery")
    print("For pickup please enter 1")
    print("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("please enter a number "))
            if delivery >= 1 and delivery <= 2 :
                if delivery == 1:
                    print("pickup")
                    break

                elif delivery == 2:
                    print("delivery")
                    break
            else:
                print("number must be 1 or 2")
            
        except ValueError:
            print("That is not a valid number")
            print("please enter 1 or 2")


# pick-up up information - name and phone



# delivery information - name address and phone number



# choose total number of pizzas - max 5



# pizza menu



# pizza ordering - from menu - print each pizza ordered with cost



# print order out - including in deliver or pick-up and names and pizza of each pizza - total cost including any deliver charge



# ability to cancel or proceed with order



# option for new order or to exit



# main function
def main():
    """
    Purpose: To run all functions
    Parameters: None
    Returns: None
    """
    welcome()
    pickup()

main()