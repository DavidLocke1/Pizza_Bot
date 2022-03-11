from os import kill


print("Do you want to start anouther order or exit")
print("To start anouther order please enter 1")
print("To exit the bot please enter 2")
while True:
    try:
        confirm = int(input("please enter a number "))
        if confirm >= 1 and confirm <= 2 :
            if confirm == 1:
                print("New order")
                break

            elif confirm == 2:
                print("Exit")
                kill
                break
        else:
            print("number must be 1 or 2")
        
    except ValueError:
        print("That is not a valid number")
        print("please enter 1 or 2")