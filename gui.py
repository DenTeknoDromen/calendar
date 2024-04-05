from tkinter import*
from tkinter import ttk
from draw_values import Draw_Values
from random import randint

v = Draw_Values()

root = Tk()
root.title("Calendar")
root.resizable(False, False)
root.geometry(v.get_window_size())

week_days = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]


#root.attributes("-alpha", 0.75)

#frame = ttk.Frame(root)
# buttons = ttk.Frame(frame)
# display = ttk.Frame(frame, borderwidth=5, relief="flat", width=1600, height=800)

toolbar = Canvas(root, width=v.get_toolbar_width(), height=v.get_toolbar_height(),background="Cyan")
toolbar.grid(row=0, column=0)

cal_vector = v.get_calendar_vector()
# Draw base gui
cnvs = Canvas(root, width=v.get_cal_width(), height=v.get_cal_height(), highlightthickness=1, highlightbackground="black", background="White")
#cnvs.create_rectangle((cal_vector[0], cal_vector[1]), (cal_vector[2], cal_vector[3]))
cnvs.create_line((cal_vector[0], cal_vector[1] + 25), (cal_vector[2], cal_vector[1] + 25))

cnvs.grid(row=0, column=1)

# Draw columns
column_width = v.get_cal_width() / 7
a = cal_vector[0]
for x in range(0, 6): 
    a += (column_width)
    cnvs.create_line((a, cal_vector[1]),(a,cal_vector[3]))

# Write top text
a = cal_vector[0]
for x in range(0,7):
    cnvs.create_text((a + (column_width/2), cal_vector[1] + 12.5), text=week_days[x], font='tkDefaeultFont 12')
    cnvs.create_text((a + (column_width * 0.03), cal_vector[1] + 28), anchor=NW, text="25 November", font='tkDefaeultFont 10')
    a += (column_width)


top_leftx = cal_vector[0] + 3
top_lefty = cal_vector[1] + 28
height_incr = v.get_cal_height() / 30
for x in range(0, 7):
    test = randint(0, 10)
    btm_rightx = top_leftx + (column_width - 6)
    for y in range(0, test):
        top_lefty += height_incr
        btm_righty = top_lefty + (height_incr * 0.8)
        cnvs.create_rectangle((top_leftx, top_lefty), (btm_rightx, btm_righty), fill="Red")
        cnvs.create_text(((top_leftx + (column_width/2)), (top_lefty + height_incr/2.5)), text="Test Text")
    top_leftx += column_width
    top_lefty = cal_vector[1] + 28

# row_height = v.get_time_row(6, 22)
# rows = v.get_time_row(6 ,22)
# for x, y in rows.items():
#     cnvs.create_text((cal_vector[0] - 10, y), text=x)
#     cnvs.create_line((cal_vector[0], y), (cal_vector[2], y))

#cnvs.pack()
root.mainloop()