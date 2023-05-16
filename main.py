from tkinter import *
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
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    global reps
    work_sec = WORK_MIN * 10
    short_break_sec = SHORT_BREAK_MIN * 10
    long_break_sec = LONG_BREAK_MIN * 10

    for i in range(12):
        reps += i
        if reps % 2 == 0:
            count_down(work_sec)
        elif reps == 8:
            count_down(long_break_sec)
        else:
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds == 0:
        canvas.itemconfig(count_text, text=f"0{count_minute}:00")
    if count_seconds < 10:
        canvas.itemconfig(count_text, text=f"0{count_minute}:0{count_seconds}")
    else:
        canvas.itemconfig(count_text, text=f"0{count_minute}:{count_seconds}")
    # print(count_seconds)
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Tracker")

# window background color
window.configure(bg=YELLOW)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bg_image)
count_text = canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(20)

header = Label(text="Timer", foreground=GREEN, font=(FONT_NAME, 45, "bold"), bg=YELLOW)
header.grid(column=1, row=0)

start_button = Button(text="Start", command=timer)
start_button.grid(column=0, row=2, ipadx=8, ipady=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2, ipadx=8, ipady=2)

check_mark = Label(text="✔", foreground=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=3, ipadx=8, ipady=2)

window.mainloop()
