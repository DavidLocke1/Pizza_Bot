# menu so that user can choose either pickup or delivery

#Bug - need to make it so that it only accepts 1 or 2


print("Is your order for pickup or delivery")

print("For pickup please enter 1")
print("For delivery please enter 2")


low = 1
high = 2

while True:
    try:
        delivery = int(input("please enter a number "))
        if delivery == 1:
            print("pickup")
            break

        elif delivery == 2:
            print("delivery")
            break

    except ValueError:
        print("Tha is not a valid number")
        print("please enter 1 or 2")
