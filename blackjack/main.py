import random
from art import logo


def deal_card():
    """this function used for get random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    """this function is used calculate the cards od players"""
    if sum(cards)==21  and  len(cards)==2:
        return 0
    if  11 in cards  and  sum(cards)==21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_scores, computer_scores):
    if user_scores==computer_scores:
        return "Draw"
    elif computer_scores==0:
        return "Lose, opponent has blackjack"
    elif user_scores==0:
        return "win with a blackjack"
    elif user_scores>21:
        return "you went over. u lose"
    elif computer_scores>21:
        return " opponent went over , u win"
    elif user_scores>computer_scores:
        return "u win"
    else:
        return "u lose"


def play():
    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)
        print(f"computer first card {computer_card[0]}")
        print(f"ur cards {user_card},current score {user_score}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("type 'y' to get another card ,type 'n' to pass")
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)

    print(f" u r final hand: {user_card},final score {user_score}")
    print(f"computer final hand {computer_card},final score {computer_score}")
    print(compare(user_score,computer_score))
while input("do u wanna play blackjack? type 'y' or 'n'.")=="y":

    print("\n"*20)
    print(logo)
    play()
