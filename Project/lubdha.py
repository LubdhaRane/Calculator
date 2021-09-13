
from tkinter import * 
import sqlite3 as sq 
import datetime

window = Tk()
window.configure(bg="lightgreen")
window.title("Exercise Tracker") 
window.geometry('800x600')
header = Label(window, text="Fitness Schedule", font=("TimesNewRoman",30,"bold"),bg="lightgreen", fg="yellow").pack()

con = sq.connect('lubdha.db') 
c = con.cursor() 

L1 = Label(window, text = "Compound Lift",bg="lightgreen", fg="navyblue", font=("TimesNewRoman", 18)).place(x=10,y=100)
L2 = Label(window, text = "Day (dd)",bg="lightgreen", fg="navyblue", font=("TimesNewRoman", 18)).place(x=10,y=150)
L3 = Label(window, text = "Month (mm)",bg="lightgreen", fg="navyblue", font=("TimesNewRoman", 18)).place(x=10,y=200)
L4 = Label(window, text = "Year (yyyy)",bg="lightgreen", fg="navyblue", font=("TimesNewRoman", 18)).place(x=10,y=250)
L5 = Label(window, text = "Max Weight (KG)",bg="lightgreen", fg="navyblue", font=("TimesNewRoman", 18)).place(x=10,y=300)
L6 = Label(window, text = "Reps",bg="lightgreen", fg="navyblue", font=("TimesNewRoman", 18)).place(x=10,y=350)


comp = StringVar(window)
comp.set('----') 

compdb = StringVar(window)
compdb.set('----')

day = StringVar(window)
month = StringVar(window)
year = StringVar(window)
weight = StringVar(window)
reps = StringVar(window)


compound = {'Bench', 'Squat', 'Deadlift','Abs'}

compd = OptionMenu(window, comp, *compound) 
compd.place(x=220,y=105)

compdbase = OptionMenu(window, compdb, *compound)
compdbase.place(x=100,y=500)

#Entry for 'input' in GUI
dayT = Entry(window, textvariable=day)
dayT.place(x=220,y=155)

monthT = Entry(window, textvariable=month)
monthT.place(x=220,y=205)

yearT = Entry(window, textvariable=year)
yearT.place(x=220,y=255)

weightT = Entry(window, textvariable=weight)
weightT.place(x=220,y=305)

repT = Entry(window, textvariable=reps)
repT.place(x=220,y=355)


def get():
        print("You have submitted a record")
        
        c.execute('CREATE TABLE IF NOT EXISTS ' +comp.get()+ ' (Datestamp TEXT, MaxWeight INTEGER, Reps INTEGER)') 
        date = datetime.date(int(year.get()),int(month.get()), int(day.get()))

        c.execute('INSERT INTO ' +comp.get()+ ' (Datestamp, MaxWeight, Reps) VALUES (?, ?, ?)',
                  (date, weight.get(), reps.get())) 
        con.commit()


        comp.set('----')
        day.set('')
        month.set('')
        year.set('')
        weight.set('')
        reps.set('')


def clear():
    comp.set('----')
    compdb.set('----')
    day.set('')
    month.set('')
    year.set('')
    weight.set('')
    reps.set('')
    
def record():
    c.execute('SELECT * FROM ' +compdb.get()) 

    frame = Frame(window)
    frame.place(x= 400, y = 150)
    
    Lb = Listbox(frame, height = 8, width = 25,font=("arial", 12)) 
    Lb.pack(side = LEFT, fill = Y)
    
    scroll = Scrollbar(frame, orient = VERTICAL) 
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set) 
    

    Lb.insert(0, 'Date, Max Weight, Reps') 
    
    data = c.fetchall()
    
    for row in data:
        Lb.insert(1,row)

    L7 = Label(window, text = compdb.get()+ '      ', 
               font=("arial", 16)).place(x=400,y=100) 
    
    L8 = Label(window, text = "They are ordered from most recent", 
               font=("arial", 16)).place(x=400,y=350)
    con.commit()

button_1 = Button(window, text="Submit",activebackground = "Skyblue",fg="orange",bg="green", font="canvas",command=get)
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Clear",activebackground = "Skyblue",fg="orange",bg="green", font="canvas",command=clear)
button_2.place(x=10,y=400)

button_3 = Button(window,text="Open",activebackground = "Skyblue",fg="orange",bg="green", font="canvas",command=record)
button_3.place(x=10,y=500)


window.mainloop() 


