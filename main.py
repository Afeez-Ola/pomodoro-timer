from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 0
seconds = 60
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    header.config(text="Timer")
    canvas.itemconfig(count_text, text=f"00:00")
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * seconds
    short_break_sec = SHORT_BREAK_MIN * seconds
    long_break_sec = LONG_BREAK_MIN * seconds

    if reps % 8 == 0:
        header.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        header.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        header.config(text="Work",fg=GREEN)
        count_down(work_sec)


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
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark += "✔"
        check_mark.config(text=mark)


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

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2, ipadx=8, ipady=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2, row=2, ipadx=8, ipady=2)

check_mark = Label( foreground=GREEN, font=(FONT_NAME, 12, "bold"), bg=YELLOW)
check_mark.grid(column=1, row=3, ipadx=8, ipady=2)

window.mainloop()
