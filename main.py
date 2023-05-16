from tkinter import *

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
window.title("Pomodoro Tracker")

window.minsize(width=500, height=300)

# window background color
window.configure(bg=YELLOW)

canvas = Canvas(width=200, height=224)

bg_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_image)
canvas.pack()

window.mainloop()
