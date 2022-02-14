# bugs
# will only work for valid input
# invalid input triggers else statement but program does not ask for input again

# menu so that user can choose either pickup or delivery

print("Do you want your order delivered or are you picking it up?")

print("for delivery enter d")
print("for pickup enter p")

delivery = input()

if delivery == "d":
    print("delivery")

elif delivery == "p":
    print("pickup")

else:
    print("That was not a valid input")