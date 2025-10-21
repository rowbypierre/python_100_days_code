from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def cyphering():
    """
    Encrypt or decrypt user text using Caesar Cipher.

    Prompt:
        - text (str): Text only containing charaters.
        - key (int): Numeral to shift. key > 0 encrypt | key < 0 decrypt.

    Returns:
        - None: Encrypted text.

    Raise:
        - ValueError: Prompt key (int) not integer.
    """
    print(logo)
    text = input("Enter text to encrypt (str): ").strip().lower()
    key = input("Enter cypher key (int): ").strip()
    if not key.isdigit() and key == "0":
        # Not accept 0;
        raise ValueError(f"Expected whole number not 0. Input: ({key})")
    else:
        key = int(key)

    alpha_len = len(alphabet)
    text_list = [char.lower() if char.isalpha() else char for char in text]
    for index, char in enumerate(text_list, start=0):
        # Replace characters only.
        if not char.isspace() and char.isalpha():
            shift = alphabet.index(char) + key

            # Reduce iterations forward and backward.
            if key > 0:
                # Encryption.
                while shift > alpha_len:
                    shift -= alpha_len
            else:
                # Decryption.
                while shift < 0:
                    shift += alpha_len

            text_list[index] = alphabet[shift]

    ciphertxt = "".join(text_list)
    print(ciphertxt)


if __name__ == "__main__":
    cyphering()
