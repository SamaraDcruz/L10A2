# Ask how many units the student used
units = int(input("Enter units used: "))

# Use simple if-else to decide the bill amount
if units <= 50:
    print("Your bill is $100")
else:
    if units <= 100:
        print("Your bill is $200")
    else:
        print("Your bill is $500")