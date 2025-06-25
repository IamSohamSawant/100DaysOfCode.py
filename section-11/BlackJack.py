import random

print('''
 ____  _            _            _    
| __ )| | __ _  ___| | _____  __| | __
|  _ \| |/ _` |/ __| |/ / _ \/ _` |/ /
| |_) | | (_| | (__|   <  __/ (_|   < 
|____/|_|\__,_|\___|_|\_\___|\__,_|\_\
                                      
.------.     .------.     .------.
|A     |     |10    |     |K     |
|  ♠   |     | ♦♦   |     | ♥♥♥  |
|     A|     |    10|     |     K|
'------'     '------'     '------'
''')

def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Returns the score calculated from the list of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares user and computer score and returns the result"""
    if user_score > 21:
        return "You went over. You lose 😭"
    if computer_score > 21:
        return "Computer went over. You win 😁"
    if user_score == computer_score:
        return "Draw 🙃"
    elif user_score == 0:
        return "Blackjack! You win 😎"
    elif computer_score == 0:
        return "Computer got Blackjack! You lose 😱"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Start of game
user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        should_continue = input("Type 'Y' to get another card, 'N' to pass: ").lower()
        if should_continue == 'y':
            user_cards.append(deal_cards())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

print(f"\nYour final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))

