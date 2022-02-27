# pizza bot program
#Bugs 23/02/2022 
#       - phone number input allows letters 
#       - name input allows numbers

import random
from random import randint
from tkinter import N

# list of random names
names = ["Mark", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Eris", "Moana", "Lewis", "Lara"]

#Cutomer details dictionary
customer_details = {}

#validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        responce = input(question)
        if responce != "":
            return responce.title()
        else:
            print("This cannot be blank")

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
def order_type():
    print("Is your order for pickup or delivery")
    print("For pickup please enter 1")
    print("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("please enter a number "))
            if delivery >= 1 and delivery <= 2 :
                if delivery == 1:
                    print("pickup")
                    pickup_info()
                    break
                elif delivery == 2:
                    print("delivery")
                    delivery_info()
                    break
            else:
                print("number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("please enter 1 or 2")

# pick-up up information - name and phone
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])
    print(customer_details)

# delivery information - name address and phone number
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print(customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question)
    print(customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question)
    print(customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question)
    print(customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question)
    print(customer_details['suburb'])
    print(customer_details)


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
    order_type()
    
main()