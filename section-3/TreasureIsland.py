print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure")
choice1=input('You\'re at a cross road. Where did you want to go? Type "left" or "right".').lower()
if choice1=="left":
    choice2=input('Do you wanna "swim" or do You wanna "wait". ').lower()
    if choice2=="wait":
        choice3=input("Through which color door you want to go (RED,BLUE,YELLOW) ,Remember this Door is one step closer to Win and Die.....   ").lower()
        if choice3=="yellow":
            print("W Mannnnnn, You Winnnnnnn")
        else:
            print("Death for choosing the Wrong color..lol")
    else:
        print("You droned in water,You died.")

else:
    print("You fell in hole. Game over.")
#This game could be more intresting I have just completed for daily task. 
