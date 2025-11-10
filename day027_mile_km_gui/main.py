from tkinter import Tk, Label, Button, Entry

FONT = ("Arial", 18, "bold")
KM_RATIO = 1.60934


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=10, pady=10)

miles_lbl = Label(text="Mile(s)", font=FONT)
miles_lbl.grid(column=3, row=0)

equal_lbl = Label(text=f"is equal to{' ' * 2}", font=FONT)
equal_lbl.grid(column=0, row=2)

km_calc_lbl = Label(text="0", font=FONT)
km_calc_lbl.grid(column=2, row=2)

km_lbl = Label(text=f"{' ' * 10}Kilometer(s)", font=FONT)
km_lbl.grid(column=3, row=2)

mile_input = Entry(width=10)
mile_input.grid(column=2, row=0)
mile_input.config(justify="center")


def calc_km():
    "Convert miles to kilometers and display at center of GUI."
    miles = mile_input.get().strip()
    if not (miles.isalpha() or miles.isspace()):
        km = float(mile_input.get()) * KM_RATIO
        km_calc_lbl.config(text=f"{km:.2f}")


calc_btn = Button(text="Calculate", command=calc_km)
calc_btn.grid(column=2, row=3)


window.mainloop()
