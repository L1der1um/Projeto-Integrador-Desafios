import tkinter as tk
from datetime import datetime

def update_clock():
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M:%S"))
    date_label.config(text=now.strftime("%A, %B %d, %Y"))
    window.after(1000, update_clock)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("300x150")

time_label = tk.Label(window, font=("Arial", 24), pady=10)
time_label.pack()

date_label = tk.Label(window, font=("Arial", 16))
date_label.pack()

update_clock()

window.mainloop()
