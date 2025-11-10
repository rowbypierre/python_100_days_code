
import pandas

az_data = pandas.read_csv("nato_phonetic_alphabet.csv")
az_phonetic = {row.letter : row.code for index, row in az_data.iterrows()}

typing = True
prompt = "Enter word: "
while typing:
    try:
        word = input(prompt)
        if len(word) == 0 or any([letter.isdigit() for letter in word]):
            raise ValueError("Word must be entered.")
        elif word.lower().strip() == "exit":
            typing = False
            break
        else:
            phonetic_word = [az_phonetic[letter] for letter in word.strip().upper()]
            print(phonetic_word)
            prompt = "\nEnter another word: "
    except Exception as error:
        print(f"Error: {error}")

