# menu so that user can choose either pickup or delivery


print("Is your order for pickup or delivery")

print("For pickup please enter 1")
print("For delivery please enter 2")


low = 1
high = 2

while True:
    try:
        delivery = int(input("please enter a number "))
        if delivery >= low and delivery <= high :
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
