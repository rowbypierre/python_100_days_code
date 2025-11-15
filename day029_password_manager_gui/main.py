# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
import json
import os
from copy import deepcopy


def save_password():
    entries = [
        entry.get().strip()
        for entry in window.winfo_children()
        if isinstance(entry, Entry)
    ]

    login_details = {entries[0]: {"Username": entries[1], "Password": entries[2]}}

    filename = "data.json"
    file_fullpath = ""
    for parent, dirs, files in os.walk("."):
        for file in files:
            if file == filename:
                file_fullpath = os.path.join(parent, file)
                break
            else:
                file_fullpath = filename

    if os.path.exists(file_fullpath) and os.path.getsize(file_fullpath) > 0:
        with open(file_fullpath, "r") as password_file:
            old = json.load(password_file)

        combined = deepcopy(old)
        for k, v in login_details.items():
            combined[k] = v
    else:
        combined = deepcopy(login_details)

    with open(file_fullpath, "w") as file_fullpath:
        json.dump(combined, file_fullpath, indent=2)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, EW
import os
import math


PADDING = 10
WINDOW_DIM = 500
CANVAS_DIM = {
    "width": math.floor(WINDOW_DIM / 2),
    "height": math.floor(WINDOW_DIM / 1.5),
}
CAVAS_ICON_XY = {
    "width": math.floor(CANVAS_DIM["width"] / 2),
    "height": math.floor(CANVAS_DIM["height"] / 2),
}

window = Tk()
window.title("MYPassword Manager")
window.geometry(f"{WINDOW_DIM + 70}x{WINDOW_DIM}")
window.config(padx=PADDING, pady=PADDING, bg="white")


icon_filename = "logo.png"
icon_path = "".join(
    os.path.abspath(os.path.join(parent, file))
    for parent, _, files in os.walk(".")
    for file in files
    if icon_filename == file
)
icon_logo = PhotoImage(file=icon_path)

taskbar_icon = icon_logo.subsample(6, 6)  # Shrink image
window.iconphoto(True, taskbar_icon)

canvas = Canvas(
    window,
    width=CANVAS_DIM["width"],
    height=CANVAS_DIM["height"],
    bg="white",
    highlightthickness=0,
)
canvas.grid(column=1, row=0)
canvas_icon = icon_logo.zoom(2)  # Enlarge 3x
canvas.create_image(
    (CAVAS_ICON_XY["width"], CAVAS_ICON_XY["height"]), image=canvas_icon
)

website_label = Label(window, text="Website:", padx=PADDING, pady=PADDING, bg="white")
website_label.grid(
    column=0,
    row=1,
    sticky=EW,
)
website_entry = Entry(window)
website_entry.grid(column=1, row=1, sticky=EW, columnspan=3)
website_entry.focus()  # Cursor


username_label = Label(
    window, text="Email/Username:", padx=PADDING, pady=PADDING, bg="white"
)
username_label.grid(column=0, row=2, sticky=EW)
username_entry = Entry(window)
username_entry.grid(column=1, row=2, sticky=EW, columnspan=3)
username_entry.insert(0, "username@domain.com")

password_label = Label(window, text="Password:", padx=PADDING, pady=PADDING, bg="white")
password_label.grid(column=0, row=3, sticky=EW)
password_entry = Entry(window)
password_entry.grid(column=1, row=3, sticky=EW, columnspan=3)

generate_button = Button(window, text="Generate Password")
generate_button.grid(column=3, row=0)

save_button = Button(window, text="Save Password", command=save_password)
save_button.grid(column=0, row=0)

window.mainloop()
