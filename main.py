'''
Written by: Chi Vo
'''


from menu_options import *


print('SUICIDE DEATH RATES IN THE U.S. FROM 1950 TO 2018\n(Note: There are some data that is unavailable...)')
userInput = int(input('\nChoose the category number you\'d like to know:\n1) Only biological sex\n2) Only race\n3) Sex and race\n'))

if userInput == 1:
    sex()
elif userInput == 2:
    race()
elif userInput == 3:
    sex_and_race()

