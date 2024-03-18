from tkinter import*
from tkinter import ttk
from draw_values import Draw_Values

v = Draw_Values()

root = Tk()
root.title("Calendar")
root.resizable(True, True)
root.geometry(v.get_window_size())


#root.attributes("-alpha", 0.75)

#frame = ttk.Frame(root)
# buttons = ttk.Frame(frame)
# display = ttk.Frame(frame, borderwidth=5, relief="flat", width=1600, height=800)

cal_vector = v.get_calendar_vector()

cnvs = Canvas(root, width=1600, height=900, background="White")
cnvs.create_rectangle((cal_vector[0], cal_vector[1]), (cal_vector[2], cal_vector[3]))
cnvs.create_line((cal_vector[0], cal_vector[1] + 50), (cal_vector[2], cal_vector[1] + 50))

column_width = v.get_cal_width() / 7
a = cal_vector[0]
for x in range(0, 6):
    a += (column_width)
    print(a)
    cnvs.create_line((a, cal_vector[1]),(a,cal_vector[3]))

row_height = v.get_time_row(6, 22)
rows = v.get_time_row(6 ,22)
for x, y in rows.items():
    cnvs.create_text((cal_vector[0] - 10, y), text=x)
    cnvs.create_line((cal_vector[0], y), (cal_vector[2], y))

cnvs.pack()
root.mainloop()