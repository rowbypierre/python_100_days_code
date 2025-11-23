import tkinter as tk
import os

def find_file(project_folder, search_file):
    file_path = None
    for parent, folders, files in os.walk("."):
        for file in files:
            if file == search_file \
            and project_folder in parent:
                file_path = os.path.join(parent, file)

    return file_path

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)


flashcard = tk.Canvas(window, width=800, height=526, bg="white")
flashcard.grid(column=0, row=0, columnspan=2)
flashcard.create_text(
    (400, 150),
    text="Arabic",
    font=("Ariel", 40, "italic")
)
flashcard.create_text(
    (400, 263),
    text="Vocabulary",
    font=("Ariel", 60, "bold")
)

wrong_image_path = find_file("day031", "wrong.png")
wrong_image = tk.PhotoImage(file=wrong_image_path)
wrong_button = tk.Button(image=wrong_image, highlightthickness=0).grid(column=0, row=1)
right_image_path = find_file("day031", "right.png")
print(right_image_path)
right_image = tk.PhotoImage(file=right_image_path)
right_button = tk.Button(image=right_image, highlightthickness=0).grid(column=1, row=1)


window.mainloop()
