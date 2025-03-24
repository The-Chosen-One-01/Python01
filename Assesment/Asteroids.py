"""The program will ask the user for the speed of an asteroid until the user put 'conclude'. Then the program will tell which asteroid is going to burn up and which is going to survive"""

#Initialise the maximum speed of the asteroid to survive, the storage to store the speed of asteroids, and the amount of asteroids that will burn up
MAXIMUM_SPEED = 11
survived_asteroids = []
burn_up = 0
FINISH = 'conclude'

#Initialise the loop for asking the user for the speed of asteroid
while True:
    try:
        
        #Ask the user for the speed of the asteroid in the form of 'float' and store it in variable 'asteroid'
        asteroid = input("Enter asteroid speed in km/s: ")
        asteroid = float(asteroid)

        #Check if the speed is negative, as it is invalid
        if asteroid < 0:
            raise ValueError

        #Check if the given speed is more than the maximum speed, if true than increment the 'burn_up' variable, as it means to will burn up
        if asteroid > MAXIMUM_SPEED:
            burn_up += 1

        #Otherwise, store the speed in the 'survived_asteroids' list
        else:
            survived_asteroids.append(asteroid)

    #Had the user did not input an integer, check if the input is 'conclude' or just some inappropriate input
    except Exception:
        if asteroid.lower() == FINISH:
            break
        print('Invalid speed.')

#Print the amount of the burned up asteroids
print(f'{burn_up} asteroids will burn up.')

#Check if any of the asteroid did survive
if survived_asteroids:

    #Iterate through each of the survived asteroids to print them
    print('The asteroids that survived were going')
    for asteroid in survived_asteroids:
        print(f'{asteroid} km/s')