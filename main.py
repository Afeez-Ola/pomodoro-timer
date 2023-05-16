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

# window background color
window.configure(bg=YELLOW)
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(width=200, height=224,bg=YELLOW)

bg_image = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=bg_image)
canvas.create_text(103,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.pack()

window.mainloop()
