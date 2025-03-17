#Initialising the storage to store the appropriate batteries and initialising the amount of voltage of minimum battery to be classify as good as well as the boundary input
batteries = []
MINIMUM = 1.2
BOUNDARY = 0

#Running a loop for asking the user batteries until the breaking point of input is inputted.
while True:
    #Checking if the input is an integer to begin with
    try:
        battery = float(input('Enter your input: '))
        
        #Checking if the battery is included in a running range of loop
        if battery < BOUNDARY:
            break
        
        #Adding the current battery as the battery is appropriate
        batteries.append(battery)
    
    #Telling the user for an integer input had the user inputted a non integer input
    except Exception:
        print('Not robot compliant!')
        
#Printing the robot's sounds with the batteries respectively
for i in batteries:
    if i >= MINIMUM:
        print('Beep')
    else:
        print('Boop')