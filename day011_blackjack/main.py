import random 
import os
from art import logo, win_ascii, lose_ascii, draw_ascii 

def blackjack():
    os.system("cls" if os.name == "nt" else "clear")

    play = input(f"{logo}Would you like to play? \n> ").lower().strip()

    while play == 'y':
            
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_hand = []
        computer_hand = []
        
        def draw(hand, deck):
            hand.append(deck[random.randint(0, len(deck) - 1)])
            return hand
        
        for card in range(2):
            player_hand = draw(player_hand, cards)
            computer_hand = draw(computer_hand, cards) 
        
        def score(hand):
            score = 0
            for card in hand:
                score += card 
            return score
                
        player_score = score(player_hand)
        computer_score = score(computer_hand)
        
        while player_score > 0:
            
            prompt1 = f"\n  Your score = {player_score} \n  Your hand = {player_hand} \n  Computer score = {computer_score} \n  Computer hand = {computer_hand}"
            print(prompt1)
            
            def win_black():
                print(logo, win_ascii)
                print(prompt1)
            
            def lose():
                print(lose_ascii)
                print(prompt1)
            
            def win():
                print(win_ascii)
                print(prompt1)
            
            def tie():
                print(draw_ascii)
                print(prompt1)
        
            if 11 in player_hand and 10 in player_hand and len(player_hand) == 2:
                win_black()
                break
            elif player_score == 21 and computer_score == 21:
                tie()
                break
            elif player_score == 21: 
                win()
                break
            elif computer_score == 21: 
                lose()
                break
            elif player_score > 21:
                if 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
                        
                    player_score = score(player_hand)
                    if player_score > 21:
                        lose()
                        break
                    elif player_score == 21: 
                        win()
                        break
                else:
                    lose() 
                    break
            elif computer_score > 21:
                if 11 in computer_hand:
                    computer_hand[computer_hand.index(11)] = 1
                        
                    computer_score = score(computer_hand)
                    if computer_score > 21:            
                        win()
                        break
                    elif computer_score == 21:            
                        lose()
                        break
                else:
                    win()
                    break
            elif player_score < 21:      
                deal = input("\nWould you like another card? \n> ").lower().strip()
                if deal == "y":
                    player_hand = draw(player_hand, cards)
                    player_score = score(player_hand)
                if computer_score < 17:
                    computer_hand = draw(computer_hand, cards)
                    computer_score = score(computer_hand) 
                elif deal != "y":   
                    if player_score < computer_score:
                        lose()
                        break
                    elif player_score > computer_score:
                        win()
                        break
                    else:
                        tie()
                        break
                                
        play = input(f"\nWould you like to play again? \n> ").lower().strip()
        
if __name__ == "__main__":
    blackjack()
    
    
    
 

