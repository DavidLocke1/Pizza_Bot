# bugs
# will only work for valid input
# invalid input triggers else statement but program does not ask for input again

# menu so that user can choose either pickup or delivery

print("Is your order for pickup or delivery")

print("For pickup please enter 1")
print("For delivery please enter 2")

delivery = int(input())

if delivery == 1:
    print("pickup")

elif delivery == 2:
    print("delivery")

else:
    print("That was not a valid input")