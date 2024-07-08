############### Blackjack Project #####################
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Funkcja która porównuje wyniki od komputera i gracza. Zwraca wynik gry
def compare(calculating_score,computer_score):
    if calculating_score == 0:
        return "You win with BlackJack!"
    if computer_score == 0:
        return "Lose, oponnent has a BlackJack!"
    if calculating_score > 21:
        return "You went over, You lose!"
    if computer_score > 21:
        return "Oponnent went over, You win!"
    if computer_score <= 21 and calculating_score <= 21:
        if computer_score > calculating_score:
            return "You lose!"
        elif calculating_score > computer_score:
            return "You win!"
        else:
            return "It's Draw!"
# Funkcja licząca wynik dla gracza wraz z zasadami
def calculating_score(player_cards):
    score = 0
    for s in player_cards:
        score = score + s
        if len(player_cards) == 2 and sum(player_cards) == 21:
            score = 0
            return score
        if 11 in player_cards and sum(player_cards) > 21:
            player_cards.remove(11)
            player_cards.append(1)
            calculating_score(player_cards)
    return score
# Funkcja licząca wynik dla komputera wraz z zasadami
def computer_score(computer_cards,player_score):
    score = 0
    for s in computer_cards:
        score = score + s
        if len(computer_cards) == 2 and sum(computer_cards) == 21:
            score = 0
            return score
        if 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
            computer_score(computer_cards,player_score)
        if score < 17 and player_score <= 21:
            computer_cards.append(random.choice(cards))
        else:
            return score

# Główna funckja gry
def blackjack():
    print(logo)
    game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").upper()
    while game == "Y":
        computer_cards = []
        computer_cards.append(random.choice(cards))
        player_cards = []
        for i in range(2):
            player_cards.append(random.choice(cards))
        score = calculating_score(player_cards)
        print(f"Your cards: {player_cards}, current score: {score} ")
        print(f"Computer's first card: {computer_cards}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").upper()
        while another_card == "Y":
            another_card = player_cards.append(random.choice(cards))
            score = calculating_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {score} ")
            print(f"Computer's first card: {computer_cards}")
            if score == 0 or score > 21:
                break
            if score < 21 and score != 0:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ").upper()
        cp_score = computer_score(computer_cards,score)
        print(f"computer's cards: {computer_cards}, computer score: {cp_score}")
        print(compare(score,cp_score))
        game = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").upper()
        print(logo)

# Wywołanie funkcji gry
blackjack()