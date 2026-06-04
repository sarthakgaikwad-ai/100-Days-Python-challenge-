rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_symbols=[rock,paper,scissors]

player_choice=int(input("What do you choose,0 for rock , 1 for paper ,2for scissors"))
if player_choice>=0 and player_choice<=2:
    print(game_symbols[player_choice])

computer_choice=random.randint(0,2)

print ("Computer choose :")
print(game_symbols[computer_choice])

if player_choice>=3 or computer_choice<0:
    print("You have entered a invalid number")

elif player_choice==0 and computer_choice==2:
    print("you win")
elif computer_choice==0 and player_choice==2:
    print("you lose")
elif computer_choice>player_choice:
    print("you lose")
elif player_choice>computer_choice:
    print("you win")
elif player_choice==computer_choice:
    print("Its a draw ")
