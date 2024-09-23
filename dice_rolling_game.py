#loop
import random

#playing = True
while True:
  choice =input('Roll the dice ? (Y/N) : ').lower()
  if choice == 'y' or choice =='Y':
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f'({die1},{die2})')
  elif choice == 'n' or choice == 'N':
    print('Thanks for playing!')
    break
  else:
    print('Invalid Choice')
