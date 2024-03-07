import time 
import os 
import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while 1 == 1:
    os.system("cls" if os.name == 'nt' else "clear")
    print("Rock, paper, scissors VS the Computer.")
    time.sleep(2)
    os.system("cls" if os.name == 'nt' else "clear")

    print("Enter 1 for rock. \nEnter 2 for paper. \nEnter 3 for scissors. \nEnter 'exit' to exit.")
    time.sleep(2)
    user_choice = input("\nEnter choice: ")
    time.sleep(2)
    if user_choice.isdigit() == True:
        user_choice = int(user_choice)
        if user_choice > 0 and user_choice < 4:
            if user_choice == 1:
                user_choice = rock
            elif user_choice == 2:
                user_choice = paper
            elif user_choice == 3:
                user_choice = scissors
                
            choices = [rock, paper, scissors]
            computer_choice = choices[random.randint(0,2)] 
            print(f"\nYour choice: {user_choice} \nComputer's choice: {computer_choice}")
            if computer_choice == rock and user_choice == scissors:
                print("\nXXXTHE COMPUTER WINSXXX")
                time.sleep(5)  
            elif computer_choice == scissors and user_choice == paper:
                print("\nXXXTHE COMPUTER WINSXXX")
                time.sleep(5)  
            elif computer_choice == paper and user_choice == rock:
                print("\nXXXTHE COMPUTER WINSXXX")
                time.sleep(5)
            elif computer_choice == user_choice:
                print("\nWE HAVE A TIE. Try again.")
                time.sleep(5)
            else:
                print("\n!!!YOU WIN!!!")
                time.sleep(5)
        
        else:
            print("\nValue must be 1, 2, or 3.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            
    elif user_choice.lower() == 'exit':
        time.sleep(2)
        sys.exit() 
             
    else:
        print("\nEnter numeric value 1, 2, or 3.")
        time.sleep(2)