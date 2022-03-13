import sys

# list to store ordered pizzas
order_list =[]
#list to store pizzas prices
order_cost =[]

#Cutomer details dictionary
customer_details = {}

print("Do you want to start anouther order or exit")
print("To start anouther order please enter 1")
print("To exit the bot please enter 2")
while True:
    try:
        confirm = int(input("please enter a number "))
        if confirm >= 1 and confirm <= 2 :
            if confirm == 1:
                print("New order")
                order_list.clear()
                order_cost.clear()
                customer_details.clear()
                main()
                break

            elif confirm == 2:
                print("Exit")
                sys.exit()
                break
        else:
            print("number must be 1 or 2")
        
    except ValueError:
        print("That is not a valid number")
        print("please enter 1 or 2")


def main():
    print("Start again")