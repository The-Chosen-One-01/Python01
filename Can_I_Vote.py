""" This program will check if the user is old enough and the resident to vote """

VOTING_AGE = 18

# Ask for user's name
while True:
    name = input('What is your name? ')
    if name:
        break
    print('Please put your name')
# Ask for user's age
while True:
    age = input('How old are you? ')
    if age.isnumeric():
        age = int(age)
        break
    print('Please put an appropriate age')
# Ask whether the user is resident or not
while True:
    resident = input('Are you a resident of New Zealand? (Y/N) ').upper()
    if resident == 'Y' or resident == 'N':
        break
    print('Please put an appropriate answer (Y or N)')

# Determine whether the user may or may not vote
if age >= VOTING_AGE and resident == 'Y':
    print(f'Congratulations {name}!!!!!! You may vote!!!!!')
else:
    print(f'Unfortunately {name}, you have not met the requirements to vote')