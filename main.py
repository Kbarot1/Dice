import random
'''
def roll_dice():
  roll = random.randint(1,6)
  print(f"you rolled a {roll}")

roll_dice()
'''

def dice_roll():
  roll = random.randint(1,6)

print("Lets play a dice game, Guess the right number and win.")
guess = input("Guess a number between 1-6:")

roll = dice_roll()
if roll == guess:
 print("You win")
elif:
  print(" ")

else:
  print("try again")
