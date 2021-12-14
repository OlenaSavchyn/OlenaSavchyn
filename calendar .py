import datetime
from tkinter import *

weekDays = ("Понеділок", "Вівторок", "Середу", "Четвер", "П'ятницю", "Суботу", "Неділю")

def clicked(event):
  sel1 = int(ent.get())
  sel2 = int(entSec.get())
  sel3 = int(entThird.get())
  data = datetime.date(sel3, sel2, sel1)
  days = data.weekday()
  resYpk = weekDays[days]
  lab['text'] = "Ви народилися в : " + resYpk

root = Tk()
root.geometry('700x450')
root.title("calendar by YPK")


lab2 = Label(text = "День:")
lab3 = Label(text = "Місяць:")
lab4 = Label(text = "Рік:")
ent = Entry(text="День", width=30)
entSec = Entry(width=30)
entThird = Entry(width=30)
but = Button(text="Порахувати")
lab = Label(width=35, height=5, bg='black', fg='white')
but.bind('<Button-1>', clicked)

lab2.pack()
ent.pack()
lab3.pack()
entSec.pack()
lab4.pack()
entThird.pack()
but.pack()
lab.pack()

root.mainloop()
