import json
import os
from copy import deepcopy
import random
import string
from tkinter import messagebox
from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, EW
import math


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def make_password():
    """
    Generate password containing letters, digits, and punctuations.

    Password inserted to password entry box on screen and copied to clipboard.

    Returns
    -------
    None
    """
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choices(list(characters), k=random.randint(10, 20)))
    password_entry.insert(0, password)
    password_entry.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_datafile():
    "Return data.json absolute path if it exist, else 'data.json'"
    filename = "data.json"
    file_fullpath = ""
    for parent, dirs, files in os.walk("."):
        for file in files:
            if file == filename:
                file_fullpath = os.path.join(parent, file)
                break
            else:
                file_fullpath = filename

    return file_fullpath


def is_valid_fields():
    """
    Check for charater in all window entries.

    Returns
    -------
    bool: True if all fields contain string else False.
    """
    fields = [website_entry, username_entry, password_entry]
    fields_valid = True
    for entry in fields:
        if len(entry.get()) == 0:
            fields_valid = False

    return fields_valid


def save_password():
    """
    Write website, username, and password to 'data.json'.

    Updates existing entries or creates the file if it doesn't exist.

    Returns
    -------
    None
    """
    if is_valid_fields():
        entries = [
            entry for entry in window.winfo_children() if isinstance(entry, Entry)
        ]
        entry_data = [entry.get().strip() for entry in entries]

        login_data = {
            entry_data[0]: {"Username": entry_data[1], "Password": entry_data[2]}
        }

        file_abspath = find_datafile()
        if os.path.exists(file_abspath) and os.path.getsize(file_abspath) > 0:
            with open(file_abspath, "r") as password_file:
                old = json.load(password_file)

            combined = deepcopy(old)
            for k, v in login_data.items():
                combined[k] = v
        else:
            combined = deepcopy(login_data)

        with open(file_abspath, "w") as file_abspath:
            json.dump(combined, file_abspath, indent=2)

        for entry in entries:
            if entry.get() != username_entry.get():
                entry.delete(0, "end")

        messagebox.showinfo(title="SUCCESS", message="Data saved.")
    else:
        messagebox.showinfo(title="ERROR", message="Check for missing inputs.")


def search_password():
    """
    Return username and password for a website entry.

    Returns
    -------
    str: Message box gui containing the credentials.

    Raises
    -------
    FileNotFound: Message box notification explaining data file is not found.
    IndexError: Message box notification explaining that data does not exist.
    """
    datafile = find_datafile()
    try:
        with open(datafile) as data:
            logins = json.load(data)
            logins = {k.upper(): v for k, v in logins.items()}
            searched_login = logins[website_entry.get().strip().upper()]
            login = f"""Username:\t{searched_login["Username"]}
                    \nPassword:\t{searched_login["Password"]}"""
            messagebox.showinfo(title="Login Information", message=login)
    except FileNotFoundError:
        messagebox.showwarning(
            title="File Not Found",
            message="There is no credentials file to retrieve your record.",
        )
    except KeyError:
        messagebox.showwarning(
            title="Record Not Found",
            message=f"Record for {website_entry.get()} not found. Please check the website link.",
        )


# ---------------------------- UI SETUP ------------------------------- #
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
canvas_icon = icon_logo.zoom(2)  # Enlarge 2x
canvas.create_image(
    (CAVAS_ICON_XY["width"], CAVAS_ICON_XY["height"]), image=canvas_icon
)

website_label = Label(window, text="Website:", padx=PADDING, pady=PADDING, bg="white")
website_label.grid(
    column=0,
    row=2,
    sticky=EW,
)
website_entry = Entry(window)
website_entry.grid(column=1, row=2, sticky=EW, columnspan=2)
website_entry.focus()  # Cursor


username_label = Label(
    window, text="Email/Username:", padx=PADDING, pady=PADDING, bg="white"
)
username_label.grid(column=0, row=3, sticky=EW)
username_entry = Entry(window)
username_entry.grid(column=1, row=3, sticky=EW, columnspan=2)
username_entry.insert(0, "username@domain.com")

password_label = Label(window, text="Password:", padx=PADDING, pady=PADDING, bg="white")
password_label.grid(column=0, row=4, sticky=EW)
password_entry = Entry(window)
password_entry.grid(column=1, row=4, sticky=EW, columnspan=2)

generate_button = Button(window, text="Generate Password", command=make_password)
generate_button.grid(column=2, row=1)

save_button = Button(window, text="Save Login", command=save_password)
save_button.grid(column=0, row=1)

search_button = Button(window, text="Search Login", command=search_password)
search_button.grid(column=1, row=1)

window.mainloop()
