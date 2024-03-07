import random, os

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

os.system("cls" if os.name == "nt" else "clear")
print("\nWelcome to the Password Generator!\n")
nr_letters = ' '
while nr_letters.isdigit() == False:
    nr_letters= input("How many letters would you like in your password?\n") 
    if nr_letters.isdigit() == False:
        print("Enter numeric value only.\n") 

nr_symbols = ' '
while nr_symbols.isdigit() == False:
    nr_symbols = input(f"How many symbols would you like?\n")
    if nr_symbols.isdigit() == False:
        print("Enter numeric value only.\n") 
        
nr_numbers = ' '
while nr_numbers.isdigit() == False:
    nr_numbers = input(f"How many numbers would you like?\n")
    if nr_numbers.isdigit() == False:
        print("Enter numeric value only.\n")


nr_letters = int(nr_letters)
nr_symbols = int(nr_symbols)
nr_numbers = int(nr_numbers)

password = ''        
for x in range(1, nr_letters + 1):
    letter = letters[random.randint(0, len(letters) - 1)]
    password += ' ' + letter

for x in range(1, nr_symbols + 1):
    symbol = symbols[random.randint(0, len(symbols) - 1)]
    password += ' ' + symbol

for x in range(1, nr_numbers + 1):
    number = numbers[random.randint(0, len(numbers) - 1)]
    password += ' ' + number   

password = password.split()
random.shuffle(password)
new_password = ''
for key in password:
    new_password += key 
print(f"\nHere is a secure password: {new_password}\n")
           