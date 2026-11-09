# CPW 101 Programming Assignment 7
# This file contains starter code for the following:

# Modify a previous program so that the user
# can use its code as many times as they wish.

CENTS_PER_QUARTER = 25 # a quarter is 25 cents
CENTS_PER_DIME = 10    # a dime is 10 cents
CENTS_PER_NICKEL = 5   # a nickel is 5 cents

total_cents = 0
# The original program calculated the value of some coins.

# get input
while True:
      invalid = False
      print('We will convert coins to cents.')
      quarters = int(input('How many quarters? '))
      if quarters < 0:
            quarters = 0 # maybe trying to add a boolan value might work
            invalid = True
      dimes = int(input('How many dimes? '))
      if dimes < 0:
            dimes = 0
            invalid = True
      nickels = int(input('How many nickels? '))
      if nickels < 0:
            nickels = 0
            invalid = True
      pennies = int(input('How many pennies? '))
      if pennies < 0:
            pennies = 0
            invalid = True
               
      # process the input,
      # calculate the total value, in cents,
      # of the coins input by the user.

      cents = CENTS_PER_QUARTER * quarters \
            + CENTS_PER_DIME * dimes \
            + CENTS_PER_NICKEL * nickels \
            + pennies + total_cents
     
      total_cents += cents

      print( quarters, 'quarters',
       dimes, 'dimes',
       nickels, 'nickels',
       pennies, 'pennies',
       'is', cents, 'cents.')

      if invalid:
            print("Can't have negitive numbers. Try again.")
            break

      ask = input(f"Do you want to convert more coins? (y/n):").strip().lower() 
      
      if ask == "y" or ask == "yes":
            continue
      else:
            break 

      

# display the original coin quantities
# and the calculated value.
# print( quarters, 'quarters',
#        dimes, 'dimes',
#        nickels, 'nickels',
#        pennies, 'pennies',
#        'is', cents, 'cents.')
