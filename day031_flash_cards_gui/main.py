import tkinter as tk
import os
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


def find_file(search_file, project_folder="day031"):
    for parent, folders, files in os.walk("."):
        for file in files:
            if search_file in file and project_folder in parent:
                return os.path.join(parent, file)

    return None


def new_arabic_word(prior_word_learned=True):
    global arabic_wordlist
    arabic_word = random.choice(
        [
            record["Arabic"]
            for record in arabic_wordlist
            if record["Arabic"] not in correct_terms
        ]
    )
    flashcard_canvas.itemconfig(flashcard_canvas_image, image=card_front_image)
    flashcard_canvas.itemconfig(
        tagOrId=study_word, text=arabic_word, fill="black", font=("Ariel", 60, "bold")
    )
    flashcard_canvas.itemconfig(word_language, text="Arabic", fill="black")

    term = flashcard_canvas.itemcget(study_word, "text")
    if prior_word_learned:
        arabic_wordlist = [
            record for record in arabic_wordlist
            if record["Arabic"] != term
            and record["English"] != term
        ]

def save_progress():
    words_unlearned_df = pandas.DataFrame.from_records(arabic_wordlist)
    words_unlearned_df.to_csv("./day031_flash_cards_gui/words_to_learn.csv")


def show_english_word(event):
    word_onscreen = flashcard_canvas.itemcget(study_word, "text")
    if word_onscreen not in [record["English"] for record in arabic_wordlist]:
        term_english = [
            record["English"]
            for record in arabic_wordlist
            if record["Arabic"] == word_onscreen
        ]
        font = (
            ("Ariel", 50, "bold")
            # if len(term_english[0]) < 10
            # else ("Ariel", 25, "bold")
        )
        flashcard_canvas.itemconfig(flashcard_canvas_image, image=card_back_image)
        flashcard_canvas.itemconfig(
            study_word, text=term_english, fill="white", font=font
        )
        flashcard_canvas.itemconfig(word_language, text="English", fill="white")



correct_terms = []
arabic_wordlist_path = find_file("arabic_wordlist_1k")
arabic_wordlist = pandas.read_csv(arabic_wordlist_path).to_dict(orient="records")


window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)

card_back_path = find_file("card_back")
card_back_image = tk.PhotoImage(file=card_back_path)
card_front_path = find_file("card_front")
card_front_image = tk.PhotoImage(file=card_front_path)
flashcard_canvas = tk.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR)
flashcard_canvas_image = flashcard_canvas.create_image(400, 263, image=card_front_image)
flashcard_canvas.grid(column=0, row=0, columnspan=2)
word_language = flashcard_canvas.create_text(
    (400, 150), text="", font=("Ariel", 40, "italic")
)
study_word = flashcard_canvas.create_text(
    (400, 263), text="", font=("Ariel", 60, "bold")
)
flashcard_canvas.bind("<Button-1>", show_english_word)


wrong_image_path = find_file("wrong")
wrong_image = tk.PhotoImage(file=wrong_image_path)
wrong_button = tk.Button(
    image=wrong_image, highlightthickness=0, command=lambda: new_arabic_word(False)
).grid(column=0, row=1)

right_image_path = find_file("right")
right_image = tk.PhotoImage(file=right_image_path)
right_button = tk.Button(
    image=right_image, highlightthickness=0, command=new_arabic_word
).grid(column=1, row=1)

new_arabic_word(prior_word_learned=False)
window.mainloop()

save_progress()