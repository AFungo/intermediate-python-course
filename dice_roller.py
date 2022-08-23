import random

def main():

  dice_rolls = int(input('How many dice would you like roll? '))
  dice_sum = 0
  dice_size = int(input('Hoe many dice would you like to roll? '))

  for i in range(0,dice_rolls):
    
    roll = random.randint(1, dice_size)
    print(f'You rolled a die a {roll}')
    dice_sum += roll

    if(roll == 1):
      print(f'you rolled a {roll}! critical fail')
    elif roll == dice_size :
      print(f'you rolled a {roll}! critical success!')
    else:
      print(f'you rolled a {roll}')

  print(f'you have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()