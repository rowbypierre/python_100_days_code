from hangman_misc import word_list, stages, logo
import random, os, time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print(logo + "\nEnjoy this hangman game.")
time.sleep(2)
print("\nA random word has been selected.")
time.sleep(2)

lives = len(stages)
lives_start = lives
guess_attempts = 0

word_choice = random.choice(word_list).lower()
word_shell = []
for count in range(0, len(word_choice)):
    word_shell.append('_')

while guess_attempts != lives_start + 1:
    clear()
    if ''.join(word_shell) == word_choice:
        print("!!!YOU WON!!!")
        print(f"\n{word_choice.capitalize()} was the mysyterious word.")
        time.sleep(2)
        break
    else:
        print(word_shell)
        # print(f"\nFor testing purposees here is the word: {word_choice}")
        lives_prompt = f"\nYou have {lives} lives."
        if lives == 1:
            print(lives_prompt.replace("lives", "life"))
        else:
            print(lives_prompt)
        user_guess = input("\nGuess a letter: ").lower().strip()
        if user_guess in word_choice and user_guess not in word_shell:
            print("\nCorrect, \"{}\" exist in the chosen word.".format(user_guess))
            time.sleep(2)
            position = 0
            for letter in word_choice:
                if letter == user_guess:
                    word_shell[position] = user_guess
                position += 1 
            print(f"\n{word_shell}")
            time.sleep(2)  
        elif user_guess in word_choice and user_guess in word_shell:
            print("\nYou have already entered the letter \"{}\".".format(user_guess)) 
            time.sleep(2)
        else:
            if lives > 1: 
                print(stages[lives - 1])
                time.sleep(2)
                lives -= 1
                guess_attempts += 1      
                print("\nIncorrect, \"{}\" does not exist in the word.".format(user_guess))
                time.sleep(2)
            else:
                clear()
                print(stages[lives - 1])
                print("\n!!!YOU WERE HUNG!!!")
                time.sleep(2)
                print(f"\n{word_choice.capitalize()} was the mysyterious word.")
                time.sleep(2)
                break     