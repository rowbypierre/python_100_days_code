import random 
import art 
import os

os.system("cls" if os.name == "nt" else "clear")
print(art.number_ascii)


difficulty = input("Enter difficulty level: \n'rookie' \n'intermediate' \n'expert' \n> ").lower().strip()
if difficulty == 'rookie':
    allowed_attempts = 10
    span = {
        "minimum" : 0,
        "maximum" : 33
    }
elif  difficulty == 'intermediate':
    allowed_attempts = 8
    span = {
        "minimum" : 0,
        "maximum" : 66
    }
elif  difficulty == 'expert':
    allowed_attempts = 6
    span = {
        "minimum" : 0,
        "maximum" : 100
    }   


game_play = True
player_guesses = 0
magic_number = random.randint(span["minimum"], span["maximum"])  
while game_play is True:
    guess = int(input(f"\nYou have {allowed_attempts - player_guesses} remaining. \nGuess a number between {span['minimum']} and {span['maximum']}. \n> ").strip())
    if guess > magic_number:
        print("Too high.")
    elif guess < magic_number:
        print("Too low.")
    elif guess == magic_number:
        print(art.win_acii + "\n!!!YOU HAVE GUESSED CORRECTLY!!!")
        game_play = False
        
    player_guesses += 1    
    if allowed_attempts ==  player_guesses:
        print(art.lose_ascii + "\n!!!YOU HAVE NO MORE ATTEMPTS!!!")
        game_play = False
        
    
        
    


