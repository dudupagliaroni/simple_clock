from tkinter import *
import datetime

root = Tk()
root.title('Relógio')
x = 600    
y = 600
canvas = Canvas(root, width=x, height=y, bg='#4682B4')
canvas.pack()

arc_sec = canvas.create_arc(240, 240, x-240, y-240, start=90, extent=-datetime.datetime.now().second*6, style=ARC, width=30, outline='#F9AE17')
arc_min = canvas.create_arc(200, 200, x-200, y-200, start=90, extent=-datetime.datetime.now().minute*6, style=ARC, width=30, outline='#F9AE17')
arc_hour = canvas.create_arc(160, 160, x-160, y-160, start=90, extent=-datetime.datetime.now().hour*30, style=ARC, width=30, outline='#F9AE17')
arc_day = canvas.create_arc(120, 120, x-120, y-120, start=90, extent=-datetime.datetime.now().day*11.61, style=ARC, width=30, outline='#F9AE17')
arc_month = canvas.create_arc(80, 80, x-80, y-80, start=90, extent=-datetime.datetime.now().month*30, style=ARC, width=30, outline='#F9AE17')
arc_year = canvas.create_arc(40, 40, x-40, y-40, start=90, extent=-datetime.datetime.now().year*3.6, style=ARC, width=30, outline='#F9AE17')


def refresh_sec():
    global arc_sec
    canvas.delete(arc_sec)
    arc_sec = canvas.create_arc(240, 240, x-240, y-240, start=90, extent=-datetime.datetime.now().second*6, style=ARC, width=30, outline='#F9AE17')
    canvas.after(1000, refresh_sec)

def refresh_min():
    global arc_min
    canvas.delete(arc_min)
    arc_min = canvas.create_arc(200, 200, x-200, y-200, start=90, extent=-datetime.datetime.now().minute*6, style=ARC, width=30, outline='#F9AE17')
    canvas.after(1000, refresh_min)

def refresh_hour():
    global arc_hour
    canvas.delete(arc_hour)
    arc_hour = canvas.create_arc(160, 160, x-160, y-160, start=90, extent=-datetime.datetime.now().hour*30, style=ARC, width=30, outline='#F9AE17')
    canvas.after(1000, refresh_hour)  

def refresh_day():
    global arc_day
    canvas.delete(arc_day)
    arc_day = canvas.create_arc(120, 120, x-120, y-120, start=90, extent=-datetime.datetime.now().day*11.61, style=ARC, width=30, outline='#F9AE17')
    canvas.after(1000, refresh_day)   

def refresh_month():
    global arc_month
    canvas.delete(arc_month)
    arc_month = canvas.create_arc(80, 80, x-80, y-80, start=90, extent=-datetime.datetime.now().month*27, style=ARC, width=30, outline='#F9AE17')
    canvas.after(1000, refresh_month)    

def refresh_year():
    global arc_year
    canvas.delete(arc_year)
    arc_year = canvas.create_arc(40, 40, x-40, y-40, start=90, extent=-datetime.datetime.now().year*3.6, style=ARC, width=30, outline='#F9AE17')
    canvas.after(1000, refresh_year)

refresh_sec()
refresh_min()
refresh_hour()
refresh_month()
refresh_day()
refresh_year()
root.mainloop()
