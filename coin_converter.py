# CPW 101 Programming Assignment 7
# This file contains starter code for the following:

# Modify a previous program so that the user
# can use its code as many times as they wish.

CENTS_PER_QUARTER = 25 # a quarter is 25 cents
CENTS_PER_DIME = 10    # a dime is 10 cents
CENTS_PER_NICKEL = 5   # a nickel is 5 cents

# The original program calculated the value of some coins.

# get input
while True:
      print('We will convert coins to cents.')
      quarters = int(input('How many quarters? '))
      dimes = int(input('How many dimes? '))
      nickels = int(input('How many nickels? '))
      pennies = int(input('How many pennies? '))
      
      if quarters < 0 or dimes < 0 or nickels < 0 or pennies < 0:
            print("Can't have negitive numbers.\nTry again.")
            break
      # process the input,
      # calculate the total value, in cents,
      # of the coins input by the user.

      cents = CENTS_PER_QUARTER * quarters \
            + CENTS_PER_DIME * dimes \
            + CENTS_PER_NICKEL * nickels \
            + pennies
     
      
      print( quarters, 'quarters',
       dimes, 'dimes',
       nickels, 'nickels',
       pennies, 'pennies',
       'is', cents, 'cents.')

      
      ask = input(f"Do you want to convert more coins? (Enter y for yes or n for no):").strip().lower() 
      
      if ask in "y" or ask in "yes":
            cents += cents 
      else:
            break 

      

# display the original coin quantities
# and the calculated value.
# print( quarters, 'quarters',
#        dimes, 'dimes',
#        nickels, 'nickels',
#        pennies, 'pennies',
#        'is', cents, 'cents.')
