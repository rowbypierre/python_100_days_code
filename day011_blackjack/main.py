import random 
import os
from art import logo, win_ascii, lose_ascii, draw_ascii 

def blackjack():
    """ 
    Blackjack game with player and computer randomly dealt two cards. 
    Player is prompted for additonal card dealings and summary of current hand, 
    computer hand, and current score.  
    """
    
    os.system("cls" if os.name == "nt" else "clear")

    play = input(f"{logo}Would you like to play? \n'y' for Yes. \n'n' for No. \n> ").lower().strip()

    while play == 'y':
            
        player_hand = []
        computer_hand = []
        
        def deal_card(hand):
            """
            Summary: Append (1) card to exist hand (dealt cards).
            
            Args:
                hand (list): Any assortment of integers representing cards.

            Returns:
                list: Current hand with addition of one randomly drawn card.
            """
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            hand.append(cards[random.randint(0, len(cards) - 1)])
            return hand
        
        for _ in range(2):
            player_hand = deal_card(player_hand)
            computer_hand = deal_card(computer_hand) 
        
        def hand_score(hand):
            """
            Summary: Determine score of current hand (dealt hand).

            Args:
                hand (list): Object storing current cards in form of integers.

            Returns:
                int: Integer value totaling summation of dealt cards.  
            """
            score = 0
            for card in hand:
                score += card 
            return score
                
        player_score = hand_score(player_hand)
        computer_score = hand_score(computer_hand)
        
        while player_score > 0:
            
            masked_prompt = f"\n  Your score = {player_score} \n  Your hand = {player_hand} \n  Computer score = {computer_hand[0]} \n  Computer hand = [{str(computer_hand[0])}{((len(computer_hand) - 1) * ', X')}]"
            unmasked_prompt = f"\n  Your score = {player_score} \n  Your hand = {player_hand} \n  Computer score = {computer_score} \n  Computer hand = {computer_hand}"
            print(masked_prompt)
            
            
            def win_black():
                """
                Summary: Print 'BLACKJACK' and 'YOU WIN' logos. Prompt final scores, user and computer hand. 
                """
                print(logo, win_ascii)
                print(unmasked_prompt)
            
            def user_lose():
                """
                Summary: Print 'YOU LOSE' logo. Prompt final scores, user and computer hand. 
                """
                print(lose_ascii)
                print(unmasked_prompt)
            
            def user_win():
                """
                Summary: Print 'YOU WIN' logo. Prompt final scores, user and computer hand. 
                """
                print(win_ascii)
                print(unmasked_prompt)
            
            def equal_hands():
                """
                Summary: Print 'DRAW' logo. Prompt final scores, user and computer hand. 
                """
                print(draw_ascii)
                print(unmasked_prompt)
            
            def determine_outcome(player_hand = player_hand, computer_hand = computer_hand, player_score = player_score, computer_score = computer_score):    
                """
                Determine if player has hit blackjack or bust.
                """
                if 11 in player_hand and 10 in player_hand and len(player_hand) == 2:
                    win_black()
                    return "break"
                elif 11 in player_hand and 10 in player_hand and len(player_hand) == 2:
                    lose_ascii
                    return "break"
                elif player_score > 21:
                    if 11 in player_hand:
                        player_hand[player_hand.index(11)] = 1
                            
                        player_score = hand_score(player_hand)
                        if player_score > 21:
                            user_lose()
                            return "break"
                        elif player_score == 21: 
                            user_win()
                            return "break"
                    else:
                        user_lose() 
                        return "break"
                elif computer_score > 21:
                    if 11 in computer_hand:
                        computer_hand[computer_hand.index(11)] = 1
                            
                        computer_score = hand_score(computer_hand)
                        if computer_score > 21:            
                            user_win()
                            return "break"
                        elif computer_score == 21:            
                            user_lose()
                            return "break"
                        else:
                            user_win()
                            return "break"
                else:
                    return "continue"

            if determine_outcome() == "break":
                break
            
            deal = input("\nWould you like another card? \n'y' for Yes. \n'n' for No. \n> ").lower().strip()
            
            if deal == "y":
                player_hand = deal_card(player_hand)
                player_score = hand_score(player_hand)
                if computer_score < 17:
                    computer_hand = deal_card(computer_hand)
                    computer_score = hand_score(computer_hand)
            else:
                if determine_outcome() == "break":
                    break
                elif player_score == computer_score:
                    equal_hands()
                    break
                elif player_score == 21 or player_score > computer_score: 
                    user_win()
                    break
                elif computer_score == 21 or player_score < computer_score: 
                    user_lose()
                    break
                
        play = input(f"\nWould you like to play again? \n'y' for Yes. \n'n' for No. \n> ").lower().strip()
        
if __name__ == "__main__":
    blackjack()
    
    
    
 

