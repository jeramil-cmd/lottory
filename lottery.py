# Lottery Numbers

import random

# initiates an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range(0, 6):
    number = random.randint(1, 49)
    # Check if this number has already been picked and ....

    while number in lotteryNumbers:
        # ....if if has, pick a new number instead
        number = random.randint(1, 19)
    # Now that we have a unique number, let's append it to our list.
    lotteryNumbers.append(number)

# Sort the list in ascending order
lotteryNumbers.sort()

userNumbers = []
for i in range(0, 6):
    number = int(input("Please enter a number between 1 and 49: "))
    while (number in userNumbers or number < 1 or number > 49):
        print("Invalid number, please try again.")
        number = int(input("Please enter a number betwween 1 and 49: "))

    userNumbers.append(number)

# Display the list on screen:
print(">> Today's lottery numbers are: ")
print(lotteryNumbers)

print(">> Your selection: ")
print(userNumbers)

counter = 0
for number in userNumbers:
    if number in lotteryNumbers:
        counter += 1

print("Your guessed " + str(counter) + " number(s) correctly.")
