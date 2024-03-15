from os import system, name
from art import logo

alphabet = ['a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 
            'y', 'z']

def encrypt():
    message = input("\nType message to encrypt: \n\n> ").strip()
    cipher_message = ''
    shifts = int(input("\nEnter number to displace each letter: \n\n> "))
    if shifts / len(alphabet) > 1:
        while True:
            shifts -= len(alphabet)
            if shifts <= len(alphabet):
                break
            
    for character in message:
        if character.isspace() or character.isalpha() == False:
            cipher_message += character
        else:
            if character.isupper():
                character = character.swapcase()
                source_uppercase = True
            position = alphabet.index(character)    
            if position + shifts > len(alphabet) - 1:
                new_character = alphabet[0 + ((position + shifts) - len(alphabet))] 
                if source_uppercase == True:
                    new_character = new_character.swapcase()
                    source_uppercase = False
                cipher_message += new_character
            else:
                new_character = alphabet[position + shifts] 
                if source_uppercase == True:
                    new_character = new_character.swapcase()
                    source_uppercase = False
                cipher_message += new_character
    print("\n" + cipher_message)

def decrypt():
    cipher_message = input("\nType message to be decrypted: \n\n> ").strip()
    decrypted_message = ''
    shifts = int(input("\nEnter number each letter is displaced by: \n\n> "))
    if shifts / len(alphabet) > 1:
        while True:
            shifts -= len(alphabet)
            if shifts <= len(alphabet):
                break
            
    for character in cipher_message:
        if character.isspace() or character.isalpha() == False:                   
            decrypted_message += character
        else:
            if character.isupper():
                character = character.swapcase()
                source_uppercase = True
            position = alphabet.index(character)
            if position - shifts < 0:
                new_character = alphabet[len(alphabet) + (position - shifts)] 
                if source_uppercase == True:
                    new_character = new_character.swapcase()
                    source_uppercase = False
                decrypted_message += new_character
            else:
                new_character = alphabet[position - shifts] 
                if source_uppercase == True:
                    new_character = new_character.swapcase()
                    source_uppercase = False
                decrypted_message += new_character
    print("\n" + decrypted_message)
 
if __name__ == "__main__":
        
    system("cls" if name == "nt" else "clear")
    print(logo)
    while True:      
        task = input("\nType: \n\"encode\"     -> encrypt \n\"decode\"     -> decrypt \n\"exit\"       -> exit \n\n> ").strip().lower()
        if task == 'encode':
            encrypt()       
        elif task == "decode":
            decrypt()
        elif task == "exit":
            break