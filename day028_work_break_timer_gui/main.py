from tkinter import Tk, Label, Canvas, PhotoImage, Button
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Work/Break Timer")
window.config(padx=50, pady=25, bg=YELLOW)


tomato_img_path = [
    os.path.join(root, file)
    for root, dirs, files in os.walk(".")
    for file in files
    if file == "tomato.png"
]
tamato_img = PhotoImage(file=tomato_img_path)

canvas = Canvas(width=200, height=300, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 180, image=tamato_img)
canvas.create_text(100, 30, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
canvas.create_text(100, 200, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=0)

start_btn = Button(text="Start", command=None, width=5, height=2)
start_btn.grid(column=0, row=1)

reset_btn = Button(text="Reset", command=None, width=5, height=2)
reset_btn.grid(column=2, row=1)

check_lbl = Label(text="☑", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
check_lbl.grid(column=1, row=2)
window.mainloop()
