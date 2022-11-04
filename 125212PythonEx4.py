"""
125212 November 4, 2022
Functions, parameters, and return values
writing a main function that calls other function
"""

import datetime

# Computes the total cost for items
def computePrice(item, price):
    return round(item * price, 2)

# Computes the shadow of an object
def shadowLength(ht):
    hour = datetime.datetime.now().hour
    return round(hour * ht, 2)

# Displays a greeting for the user
def greeting():
    hour = datetime.datetime.now().hour
    if 0 < hour <= 11:
        print("Good Morning!")
    elif 12 < hour <= 17:
        print("Good Afternoon!")
    elif 18 < hour <= 21:
        print("Good Evening!")
    else:
        print("Good Night!")

# Computes an employee's weekly salary
def salary(hours):
    wage = (40 * 11.3) + ((hours - 40) * 1.5 * 11.3)
    return wage

# Main function that displays a menu and calls the appropriate functions
def main():
    print("Welcome to my function exercises. I am using a return statement, \
parameters, arguments and paying attention to the syntax of defining functions")
    print("""1. Compute price of items 
2. Compute shadow of an object 
3. Print Greeting
4. Compute employee's weekly salary 
""")
    choice = int(input("Please choose one: "))

# If statement for the function the user wants to use
    if choice == 1:
        items = int(input("Enter the number of items: "))
        price = float(input("Enter the price for the item: "))
        print("The price of", items, "items is", computePrice(items, price), "dollars.")
    elif choice == 2:
        height = float(input("Enter the height of the object: "))
        print("The shadow length of an object with", height, "is: ", shadowLength(height))
    elif choice == 3:
        greeting()
    else:
        hours = int(input("Enter the amount of hours: "))
        print("This is the worker's weekly salary: ", salary(hours))
        
# Obtaining input about if they want to use the function
ans = str(input("Would you like to try my functions? y/n: ")).lower()
while ans[0] == "y":
# Calling the main function
    main()
    ans = str(input("Would you like to try my functions agian? y/n: ")).lower()
print("Thanks for using my functions. Goodbye!")
