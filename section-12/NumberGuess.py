import random
def play_again():
    print(
        """"
        ________                                                                 ___.                 
    /  _____/ __ __   ____   ______ ______    _____         ____  __ __  _____\_ |__   ___________ 
    /   \  ___|  |  \_/ __ \ /  ___//  ___/    \__  \       /    \|  |  \/     \| __ \_/ __ \_  __ 
    \    \_\  \  |  /\  ___/ \___ \ \___ \      / __ \_    |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
    \______  /____/  \___  >____  >____  >    (____  /    |___|  /____/|__|_|  /___  /\___  >__|   
            \/            \/     \/     \/          \/          \/            \/    \/     \/       
        """""
    )
    print("Welcome to the Number Guessing Game! ")
    print("I'am thinking of a number between 1 and 100.")
    difficulty=input("Choose a dificulty. Type 'easy' or 'hard': ").lower()
    easy_trys=10
    hard_trys=5
    numbers = list(range(1, 101))
    random_choice=random.choice(numbers)
    
    if difficulty=="easy":
        while int(easy_trys)>0:
            
            guess=int(input("Make a guess: "))
            if guess>random_choice:
                print("Too high")
                print("Guess again")
                easy_trys = str(int(easy_trys) - 1)
                print(f"You have {easy_trys} attempts remaining to guess the number.")
                
            elif guess<random_choice:
                print("Too low")
                print("Guess again")
                easy_trys = str(int(easy_trys) - 1)
                print(f"You have {easy_trys} attempts remaining to guess the number.")
                
            elif guess==random_choice:
                print("You guessed it!")
                print(f"The Answer was {random_choice}")
                break
        else:
            print(f"You've run out of guesses. The answer was {random_choice}")


    if difficulty=="hard":
        while int(hard_trys)>0:
            
            guess=int(input("Guess a number: "))
            if guess>random_choice:
                print("Too high")
                print("Guess again")
                hard_trys=str(int(hard_trys)-1)
                print(f"You have {hard_trys} attempts remaining to guess the number.")
            elif guess<random_choice:
                print("Too Low")
                print("Guess again")
                hard_trys=str(int(hard_trys)-1)
                print(f"You have {hard_trys} attempts remaining to guess the number.")
            elif guess==random_choice:
                print("You guessed it!")
                print(f"The Answer was {random_choice}")
                break
        else:
            print(f"You've run out of guesses. The answer was {random_choice}")

while True:
    play_again()
    again=input("Do you want to play again.Type 'Yes' or 'No'.").lower()
    if again!="yes":
        print("GoodBye")
        break