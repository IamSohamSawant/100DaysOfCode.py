import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''',]
word_list = [
    "dog", "cat", "hat", "sun", "tree", "car", "fish", "bird", "moon", "cup", 
    "apple", "mop", "star", "bed", "shoe", "ball", "fox", "bush", "frog", "deer", 
    "rock", "rain", "cap", "bed", "fan", "poo", "bee", "milk", "start", "cake", 
    "bus", "pencil", "spoon", "van", "pear", "book", "duck", "egg", "flag", "ship", 
    "soap", "lamp", "bread", "pot", "rose", "boot", "mug", "key", "hand", "nail", 
    "doll", "bag", "fig", "hog", "hat", "net", "nook", "star", "box", "toad", "boat", 
    "car", "cup", "pen", "tree", "boa", "bat", "fork", "bell", "sun", "kite", "drum", 
    "hen", "ice", "coat"
]


lives=6
print("""
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                         
                             888                              
                        Y8b d88P                              
                         "Y88P"              """)

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

game_over=False
correct_letters=[]
while not game_over:
    print(f"**********{lives}/6 LIVES LEFT**********")
    guess=input("Guess a letter :").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display=""

    for letter in chosen_word:   
         if letter == guess:
            display+=letter
            correct_letters.append(guess)
         elif letter in correct_letters:
             display+=letter
         else:
            display+="_"
    print(display)

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess} that's not in the word. You lose a life.")
        if lives==0:
            game_over=True    
            print(f"**********It was {chosen_word}! You Lose**********")
           

    if "_"  not in display:
         game_over=True
         print("**********You Win**********")
    
    print(stages[lives])
   