""" This program will check to see of the userhas entered a vaild integer"""
# Use constant for the low and high values
LOW = 1
HIGH = 10
# Ask the user to type in a number
num = input("Please enter an integer: ")

# Check to see if the number is valid
if num.lstrip('-').isnumeric():
    num = int(num)
    if num < LOW:
        print(f'{num} is lower than {LOW}') #Low
    elif num > HIGH:
        print(f'{num} is greater than {HIGH}') #High
    else:
        print(f'Your number is {num}') #Ok
else:
    print(f"{num} is not an integer") #Wrong