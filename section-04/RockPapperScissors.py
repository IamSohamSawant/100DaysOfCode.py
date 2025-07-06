import random
user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices={
    "rock": """ Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """ Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """ Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

if user_chose== 0:
    user_choice= "rock"
elif user_chose== 1:
    user_choice= "paper"
elif user_chose==2:
    user_choice="scissors"
else:
    print("Invalid Input")
    exit()
print(f"\nYou chose:\n{choices[user_choice]}")


computer_choice =random.choice(list(choices.keys()))
print(f"Computer chose:\n{choices[computer_choice]}")


if user_choice == computer_choice:
    print("It's a Tie!")
elif (user_choice=="rock" and computer_choice=="scissors") or \
     (user_choice=="paper" and computer_choice=="rock") or \
     (user_choice=="scissors" and computer_choice=="paper"):
    print("You Win!")
else:
    print("You Lose!")
