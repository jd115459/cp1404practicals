"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    An example of a ValueError is when a user is prompted to input an age and the user types out 'seven' instead of
    typing in the integer 7.
2. When will a ZeroDivisionError occur?
    When any number is divided by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    You could change the code to check if the user has entered a zero and if they have, print a message and let them
    try again using a while loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")