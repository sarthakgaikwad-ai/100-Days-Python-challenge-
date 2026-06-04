print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1=input('Your\'re at ht crossroad,'
               'Where do you want to go? '
               'Type ''"left" or "right"').lower()#.lower for converting the whole text in lowercase

if choice_1=="left":
    choice_2=input('You\'ve hae come to the lake.'
          'There is a island in the middle of the lake .'
          'Type "wait" for a boat.'
          'Type "swim" to swim across.\n').lower()
    if choice_2=="wait":
        choice_3=input("You have arrived at the island unharmed.'"
                       "There is a house with 3 doors red,yellow and blue."
                       "Which colour do you choose.\n").lower()
        if choice_3=='red':
            print("You've landed in room full of fire.Game over")
        elif choice_3=='yellow':
            print("You have found the treasure,You win")
        elif choice_3=='blue':
            print("You have fallen in room full of snow.Game over")
        else:
            print("You have choose the door that does not exist.Game over")

    else:
        print("You got attacked by sharks.Game Over")
else:
    print("You have fallen in the hole.Game over")

