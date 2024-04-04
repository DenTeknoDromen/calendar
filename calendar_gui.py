import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("600x400")
root.title('Calendar')
#root.resizable(0, 0)

days_to_display = 7
weekdays = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

hours_to_display = [6, 21]
time = hours_to_display[1] - hours_to_display[0]

# configure the grid
root.columnconfigure(0, weight=1)
for x in range(1, days_to_display + 1):
    root.columnconfigure(x, weight=2)

for y in range(1, time + 1):
    root.rowconfigure(y, weight=2)

# blank_cell = ttk.Label(root)
# blank_cell.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

def test_click(event):
    print("Click")

for days in range (1, days_to_display + 1):
    days_col = tk.Frame(root, relief="sunken", background="Blue") #text=weekdays[days - 1]/*, background="Blue")
    days_col.grid(column=days, row=0, sticky=tk.W)
    days_col.bind("<Button-1>", test_click)


for hours in range(1, time + 1):
    time_row = ttk.Label(root, text=f"kl: {hours + hours_to_display[0]}", background="Yellow")
    time_row.grid(column=0, row=hours, sticky=tk.W,)

test = ttk.Label(root, background="Red")
test.grid(column=1, row=1, rowspan=5)
    

#username_entry = ttk.Entry(root)
#username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
#password_label = ttk.Label(root, text="Password:")
#password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

#password_entry = ttk.Entry(root,  show="*")
#password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
#login_button = ttk.Button(root, text="Login")
#login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


root.mainloop()