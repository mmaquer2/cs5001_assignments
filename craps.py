'''
Michael Maquera
CS 5001 HW 3
Fall 2020

Craps.py

'''

import random

def roll_again(point):
 rolls = 0
 goal_number = point
 #use this infinte while loop to keep running the roll function
 # as long as the user wants to continue
 while( 1 > 0 ):
 #get two random numbers from 1 to 6 to represent the dice
  num1 = random.randint(1,6 )
  num2 = random.randint(1,6)
  # add the numbers together for the sum of the round
  score = int(num1 + num2)
  continue_game_status= str(input('hey would you like to continue or exit? (c/e) '))
  if( continue_game_status == 'e'):
   print('okay then maybe next time!')
   break
  elif(score == 7):
   print(' you rolled a ', num1 ,'+' , num2)
   print('sorry you rolled a 7, you lost!')
   break
  elif(score == goal_number):
   print(' you rolled a ', num1 ,'+' , num2)
   print('congrats you rolled your point again after')
   break
 print(' you rolled a ', num1 ,'+' , num2)
 print('you rolled a ', score)
                  
def play_craps():
    #start the first round by simulating two dice
 num1 = random.randint(1,6)
 num2 = random.randint(1,6) 
 roll_one = int(num1 + num2)
 print(' you rolled a ', num1 ,'+' , num2)
 if roll_one == 12 and 2 and 3:
  print('you lost, sorry! you rolled a ', roll_one)
 elif(roll_one == 7 and 11):
  print('you rolled a', roll_one, 'congrats you won!')
 else:
   print('you rolled a', roll_one)
   print('lets roll again')
   roll_again(roll_one)
                
def main():
 start= str(input('hey would you like to play craps with us? y/n '))
 if (start == 'y'):
  print('awesome! lets play! ')
  play_craps()
 else:
  print('okay then..maybe another time')


main()
