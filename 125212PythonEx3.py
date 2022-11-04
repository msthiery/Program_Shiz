"""
125212 November 1, 2022 Functions and for loop
Learning to write a function with parameters and
calling them with arguments
"""

# Function to convert to th erequested base
def convert(decimal, base):
    conNum = ''
    rem = 0
    while decimal >= 1:
        rem = decimal % base
        if rem == 10:
            rem = 'A'
        elif rem == 11:
            rem = 'B'
        elif rem == 12:
            rem = 'C'
        elif rem == 13:
            rem = 'D'
        elif rem == 14:
            rem = 'E'
        elif rem == 15:
            rem = 'F'
        conNum = str(rem) + conNum
        decimal = decimal//base
    return conNum

# Function to display the chain of numbers
def chain(origin, base):
    link = str(origin)
    dash = '-'
    while origin >= base:
        origin = origin // base
        link = str(origin) + dash + link
    return link

ans = input("Would you like to try my functions? y/n: ").lower()
while ans[0] == 'y':
    number = int(input("Give me a positive integer that you want \
to convert: "))
    base = int(input("Give me a base you would like to convert to (2, 8, 16): "))
    
# Output of the user's number
    print("The number that you gave is: ", number)
    print("The conversion is: ", convert(number, base))
    print("The chain of your number is: ", chain(number, base))
    
    ans = input("Would you like to try my functions again? y/n: ").lower()
print("Thank you for using my functions. Goodbye.")