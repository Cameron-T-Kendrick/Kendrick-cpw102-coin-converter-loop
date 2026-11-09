CENTS_PER_QUARTER = 25 
CENTS_PER_DIME = 10    
CENTS_PER_NICKEL = 5   

total_cents = 0

while True:
      invalid = False
      print('We will convert coins to cents.')
      quarters = int(input('How many quarters? '))
      if quarters < 0:
            quarters = 0 
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

      



