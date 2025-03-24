""" This program will ask the amount for every flavours of pizza and print them, except if the amount is 0"""

#Initialise the flavours of pizzas, the ignored number, and the storage to store the amount of each pizzas
IGNORED_NUM = 0
flavours = ['cheese','chicken','pepperoni','veggie']
amounts = {}

#Going through every pizza flavours
for flavour in flavours:

    #Keep asking for the appropriate amount of pizza flavour
    while True:
        try:

            #Store the input of amount in 'string' type 
            pizza = input(f'How many {flavour} pizzas do we want? ')

            #Checking if the input includes a coma sign, decimal point, or minus sign
            if '.' in pizza or ',' in pizza or '-' in pizza:
                raise ValueError
            
            #Changing the 'string' amount of pizza to 'integer' amount of pizza
            pizza = int(pizza)

            #With all invalid input eliminated, store the amount in a dictionary and break the 'while' loop
            amounts[flavour] = pizza
            break
        
        #Had the user gave an invaild input, tell the user about it
        except Exception:
            print('Please enter a vaild input')

#With all the flavours being asked and given the appropriate input, begin to go through every given amounts for every flavours
for flavour in amounts:

    #Initialise the amount of each pizza
    pizza_amount = amounts[flavour]

    #Check if the amount of pizza is not the ignored number
    if pizza_amount != IGNORED_NUM:
        print(f'{flavour.title()}: {pizza_amount}')