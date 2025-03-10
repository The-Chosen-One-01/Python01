"""This program asks the user for their name and favourite numbers
and then perform simple math on the numbers"""

# Ask the user for their name and favourite numbers
name = input("What's your name? ")
num1 = int(input("What's your favourite number? "))
num2 = int(input("What's your second favourite number? "))

# Perform some simple maths on the numbers
add = num1 + num2
multiply = num1 * num2

# Greet the user amd print the result
print(f'Hi {name}, here are some fun calculations with your favourite numbers')
print(f'{num1} + {num2} = {add}')
print(f'{num1} x {num2} = {multiply}')