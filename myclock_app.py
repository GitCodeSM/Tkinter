import tkinter as tk
import datetime
from datetime import datetime
from cv2 import FONT_HERSHEY_COMPLEX

# create window for the app
window = tk.Tk()

# title for our window
window.title("Today's date and time!")

# geometry of the window
window.geometry('400x400')

# getting present date and time
time_now = datetime.now()
today = datetime.today()
mydatetime = datetime(today.year, today.month, today.day, time_now.hour, time_now.minute, time_now.second, time_now.microsecond)
today_dt = mydatetime.ctime()

# checkbox
button = tk.Checkbutton(activeforeground="#000fff000", text="Show Date & Time")
button.grid(column=0, columnspan=5, row=0, rowspan=2)
button.bbox(column=0, row=0, col2=2, row2=0)

#button.pack() for placing button in centre

# add a text using label method
t = today_dt.split()
for i in range(len(t)):
    t[i] = t[i].capitalize()

newlabel = tk.Label(font=FONT_HERSHEY_COMPLEX, highlightbackground="#00ffff", foreground="#000fff000", highlightthickness=10, text = ' '.join(t))

#placing on the grid
newlabel.grid(column=5, row=5)

tk.mainloop()
