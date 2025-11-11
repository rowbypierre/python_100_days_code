from tkinter import Tk, Label, Canvas, PhotoImage, Button
import os
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MIN_SECS = 60
round = 0
final_round = 8
window_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    "Start a Pomodoro timer, update UI for current round."

    window.after_cancel(window_timer)
    global canvas
    canvas.itemconfig(canvas_timer, text="00:00")
    checks_lbl.config(text=None)
    canvas.itemconfig(canvas_logo, text="Timer")
    global round
    round = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(min=WORK_MIN):
    global round, final_round
    round += 1
    round_str = "Work"
    round_logo_format = {
        "font": {"Work": 30, "Long Break": 20, "Short Break": 20},
        "fill_color": {"Work": GREEN, "Long Break": RED, "Short Break": PINK},
    }

    if final_round == round:
        min = LONG_BREAK_MIN
        round_str = "Long Break"
    elif round % 2 == 0:
        min = SHORT_BREAK_MIN
        round_str = "Short Break"
        work_sessions = math.floor(round / 2)
        marks = "☑" * work_sessions
        checks_lbl.config(text=marks)

    canvas.itemconfig(
        canvas_logo,
        text=round_str,
        fill=round_logo_format["fill_color"][round_str],
        font=(FONT_NAME, round_logo_format["font"][round_str], "bold"),
    )
    timer(min * MIN_SECS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_fomat(x):
    "Return signal digit as string with '0' prefix."
    return "0" + str(x) if x < 10 else x


def timer(max_secs):
    """Countdown timer updating the canvas every second.

    Parameters:
        - max_secs (int): Total seconds to count down.
    """
    minutes = math.floor(max_secs / MIN_SECS)
    seconds = max_secs % MIN_SECS

    canvas.itemconfig(
        canvas_timer, text=f"{timer_fomat(minutes)}:{timer_fomat(seconds)}"
    )
    if max_secs > 0:
        global window_timer
        window_timer = window.after(1000, timer, max_secs - 1)
    else:
        start_timer()


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
canvas_logo = canvas.create_text(
    100, 30, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold")
)
canvas_timer = canvas.create_text(
    100, 200, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(column=1, row=0)

start_btn = Button(text="Start", command=start_timer, width=5, height=2)
start_btn.grid(column=0, row=1)

reset_btn = Button(text="Reset", command=reset_timer, width=5, height=2)
reset_btn.grid(column=2, row=1)

checks_lbl = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
checks_lbl.grid(column=1, row=2)

window.mainloop()
