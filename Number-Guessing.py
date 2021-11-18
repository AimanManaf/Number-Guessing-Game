import random

max_guess = 10
num_digit = 3

def main():
  print('Hello and welcome to this number guessing game!\n\nThe purpose of this game is to guess a number randomly generated.\n')
  print('You need to guess a 3 digit number and each time you guess, there will be cluess given until you guess it right.')
  print('Good Luck!\n')

  while True:
    print('\nI have thought up a number.')
    print('You have 10 guesses and clues will be given for each guess\n')
    
    secretNum = getsecretNumber()

    numGuesses = 1
    while numGuesses <= max_guess:
      guess = ''

      while len(guess) != num_digit:
        print('\nGuess',numGuesses,': ')
        guess = input('> ')
        


      clues = getClues(guess,secretNum)
      print(clues)
      numGuesses += 1

      if guess == secretNum:
        break
      
    print('\nYou ran out of guesses. The answer is', secretNum)
    play = input('Do you want to keep playing? (y/n): ').lower()

    if play == 'y':
      continue
    
    else: 
      print('Thanks for playing !')
      quit()




def getsecretNumber():    #store the number that need to be guessed
  number = list('0123456789')
  random.shuffle(number)
  secret_number = ''
  
  for i in range(num_digit):
    secret_number = secret_number + str(number[i])
  
  return secret_number

def getClues(guess,secret_number):
  if guess == secret_number:
    print('Congratulations! You guess it right!')

  clues = []

  for i in range(len(guess)):
    if guess[i] == secret_number[i]:
      clues.append('One digit is correct and at the right position.')

    elif guess[i] in secret_number:
      clues.append('One digit is correct but at the wrong position.')

  if len(clues) == 0:
    print('You have no correct digit! Try again')
  
  else:
    clues.sort()
    return ' AND '.join(clues)




main()
    



