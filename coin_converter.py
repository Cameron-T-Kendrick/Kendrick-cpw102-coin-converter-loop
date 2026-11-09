# CPW 101 Programming Assignment 7
# This file contains starter code for the following:

# Modify a previous program so that the user
# can use its code as many times as they wish.

CENTS_PER_QUARTER = 25 # a quarter is 25 cents
CENTS_PER_DIME = 10    # a dime is 10 cents
CENTS_PER_NICKEL = 5   # a nickel is 5 cents

# The original program calculated the value of some coins.

# get input
def cents_nums(cents):

      print('We will convert coins to cents.')
quarters = int(input('How many quarters? '))
dimes = int(input('How many dimes? '))
nickels = int(input('How many nickels? '))
pennies = int(input('How many pennies? '))

# process the input,
# calculate the total value, in cents,
# of the coins input by the user.

cents = CENTS_PER_QUARTER * quarters \
      + CENTS_PER_DIME * dimes \
      + CENTS_PER_NICKEL * nickels \
      + pennies

while True:
      
      ask = input("Do you want to convert more coins? (y/n): ").strip().lower()
      if ask not in ("y", "yes"):
        break
      
      # if quarters >= 0:
      #       print(f"Do you want to convert more coins? (Enter y for yes):")
      #       continue
      # elif dimes >= 0:
      #       print(f"Do you want to convert more coins? (Enter y for yes):")
      #       continue
      # elif nickels >= 0:
      #       print(f"Do you want to convert more coins? (Enter y for yes):")
      #       continue
      # elif pennies >= 0:
      #       print(f"Do you want to convert more coins? (Enter y for yes):")
      #       continue
      # else: 
      #       break

# display the original coin quantities
# and the calculated value.
print( quarters, 'quarters',
       dimes, 'dimes',
       nickels, 'nickels',
       pennies, 'pennies',
       'is', cents, 'cents.')



#  incert_coin = cents_nums(cents)
      # for incert_coin in cents:
      #       ask = input(f"Do you want to convert more coins? (Enter y for yes or n for no):")
      # for _ in ask:
      
      #       if ask.strip().lower() == "y" or ask.strip().lower() == "yes":
      #             continue
      #       elif ask.strip().lower() == "n" or "no":
      #             break