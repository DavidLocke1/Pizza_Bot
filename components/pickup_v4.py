#Cutomer details dictionary
from operator import not_


customer_details = {}

def not_blank(question):
    valid = False
    while not valid:
        responce = input(question)
        if responce != "":
            return responce
        else:
            print("This cannot be blank")

#Basic Instructions
question = ("Please enter your name ")
customer_details['name'] = not_blank(question)
print(customer_details['name'])

question = ("Please enter your phone number ")
customer_details['phone'] = not_blank(question)
print(customer_details['phone'])