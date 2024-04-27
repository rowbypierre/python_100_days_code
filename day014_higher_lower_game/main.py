import art, random, os, time, game_data
def higher_lower_game():
    """
    Determine social media account with greater number of followers. Gameplayers input (numeric value '1' or '2') required
    to play this game. If the user successfully completes 49 comparison, they are prompted to play the game again.
    """
    print(art.logo + "\nGuess the person or organization with MORE social media followers?")

    data = game_data.data
    random.shuffle(data)
    dataset_size = len(data)
    continue_play = True

    while continue_play is True:
        def clear_screen():
            """
            Clear terminal screen (windows or linux OS).
            """
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
        
        clear_screen()
        account1 = data[random.randint(0, dataset_size - 1)]
        iteration = 0

        for x in range(dataset_size):
            game_streak = iteration  
            iteration += 1
            
            account2 = data[x]
            if account2["name"] == account1["name"]:
                pass
            else:
                print(f"# CORRECT:\t{game_streak}")
                print(f"\nAccount 1: \nName\t\t- {account1['name']}, \nDescription\t- {account1['description']}, \nCountry\t\t- {account1['country']}")
                print(art.vs)
                print(f"Account 2: \nName\t\t- {account2['name']}, \nDescription\t- {account2['description']}, \nCountry\t\t- {account2['country']}")
                user_guess = int(input(f"\nWho has more followers? \nEnter 1 --> {account1['name']} \nEnter 2 --> {account2['name']} \n> "))

                if account1['follower_count'] > account2['follower_count']:
                    correct_answer = 1
                else: 
                    correct_answer = 2
                
                if user_guess == correct_answer:
                    print(art.right + f"{account1['name']} has {account1['follower_count']} million followers.")
                    print(f"{account2['name']} has {account2['follower_count']} million followers.")
                    if correct_answer == 2:
                        account1 = account2
                    clear_screen()    
                else:
                    print(art.wrong)
                    continue_play = False
                    clear_screen()
                    break
            
            if iteration == dataset_size and input("\nWould you like to play again? \nEnter 'y'\t--> Yes. \nEnter 'n'\t--> No. \n> ").strip().lower() == 'y':
                continue_play = True
            else:
                continue_play = False    
                
if __name__ == "__main__":
    higher_lower_game()
    
    