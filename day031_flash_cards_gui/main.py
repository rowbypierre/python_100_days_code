import tkinter as tk
import os
import pandas
import random
import unicodedata

BACKGROUND_COLOR = "#B1DDC6"


def get_fullpath(search_file, project_folder="day031"):
    """
    Returns aboslute path of file withing project folder.

    Parameters
    -----------
    search_file (str): File name, excluding file format.
    project_folder (str): Parent folder, project folder as default.

    Returns
    --------
    str: Aboslute file path.
    None: If file not found.
    """
    for parent, folders, files in os.walk("."):
        for file in files:
            if search_file in file and project_folder in parent:
                return os.path.join(parent, file)

    return None


def plain_word(word):
    """
    Return NFC-Normalized version of the text.
    Note: Arabic letters can be stored in slightly different hidden ways.
    """
    return unicodedata.normalize("NFC", word)


def get_arabic_word(last_word_learned=True):
    """
    Return arabic word.

    Parameters
    -----------
    prior_word_learned (bool):  Default True - if previous on screen Arabic learned else False.
                                Note: True --> previous term removed from deck (word list).

    Returns
    --------
    None: English word translated in Arabic.
    """
    global arabic_words_dict, learned_words
    last_word = flashcard_canvas.itemcget(flashcard_word, "text")
    if last_word_learned:
        arabic_words_dict = [
            record
            for record in arabic_words_dict
            if record["Arabic"] != last_word and record["English"] != last_word
        ]

    arabic_word = random.choice(
        [
            record["Arabic"]
            for record in arabic_words_dict
            if record["Arabic"] not in learned_words
        ]
    )
    arabic_word = plain_word(arabic_word)
    flashcard_canvas.itemconfig(flashcard_canvas_image, image=card_front_image)
    flashcard_canvas.itemconfig(
        tagOrId=flashcard_word,
        text=arabic_word,
        fill="black",
        font=("Ariel", 60, "bold"),
    )
    flashcard_canvas.itemconfig(word_language, text="Arabic", fill="black")


def save_progress():
    "Save Arabic terms (not reviewed or incorrect translation) as CSV file."
    global arabic_words_dict
    words_unlearned_df = pandas.DataFrame.from_records(arabic_words_dict)
    words_unlearned_df.to_csv("./day031_flash_cards_gui/study_words_flashy.csv")


# TRANSLATE ARABIC TEXT TO ENGLISH (ONSCREEN WITHIN WINDOW)
def show_english_word(event):
    "Flip onscreen flashcard to back and replace Arabic text with translated English text."
    arabic_word = plain_word(flashcard_canvas.itemcget(flashcard_word, "text"))

    global arabic_words_dict
    flashcard_flipped = arabic_word.isascii()
    if not flashcard_flipped:
        english_word = ""
        for record in arabic_words_dict:
            if arabic_word in plain_word(record["Arabic"]):
                english_word = record["English"]
                break

        english_word_len = len(english_word[0])
        font_size = 50 if english_word_len < 10 else 25
        font = ("Ariel", font_size, "bold")

        flashcard_canvas.itemconfig(flashcard_canvas_image, image=card_back_image)
        flashcard_canvas.itemconfig(word_language, text="English", fill="white")
        flashcard_canvas.itemconfig(
            flashcard_word, text=english_word, fill="white", font=font
        )


# WORDS (LEARNED AND UNLEARNED)
learned_words = []
arabic_wordlist_path = get_fullpath("study_words_flashy") or get_fullpath(
    "arabic_wordlist_1k"
)
arabic_words_dict = pandas.read_csv(arabic_wordlist_path).to_dict(orient="records")

# MAIN WINDOW
window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)

# FLASH CARD (FRONT AND BACK)
card_back_path = get_fullpath("flashcard_back")
card_back_image = tk.PhotoImage(file=card_back_path)
card_front_path = get_fullpath("flashcard_front")
card_front_image = tk.PhotoImage(file=card_front_path)
flashcard_canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR)
flashcard_canvas_image = flashcard_canvas.create_image(400, 263, image=card_front_image)
flashcard_canvas.grid(column=0, row=0, columnspan=2)
word_language = flashcard_canvas.create_text(
    (400, 150), text="", font=("Ariel", 40, "italic")
)
flashcard_word = flashcard_canvas.create_text(
    (400, 263), text="", font=("Ariel", 60, "bold")
)
flashcard_canvas.bind("<Button-1>", show_english_word)

# X OR WRONG BUTTON
wrong_image_path = get_fullpath("wrong_button")
wrong_image = tk.PhotoImage(file=wrong_image_path)
wrong_button = tk.Button(
    image=wrong_image, highlightthickness=0, command=lambda: get_arabic_word(False)
).grid(column=0, row=1)

# CHECK OR CORRECT BUTTON
correct_image_path = get_fullpath("right_button")
correct_image = tk.PhotoImage(file=correct_image_path)
correct_button = tk.Button(
    image=correct_image, highlightthickness=0, command=lambda: get_arabic_word(True)
).grid(column=1, row=1)

# OPEN WINDOW WITH FLASHCARD WITH ARABIC WORD TO BEGIN STUDYING
get_arabic_word(last_word_learned=False)

# START GUI LOOP, WINDOW REMAINS OPEN UNLESS CLOSED BY USER
window.mainloop()

# SAVE WORD(S) NOT REVIEWED NEEDING MORE STUDY TO CSV
save_progress()
