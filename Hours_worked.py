# Building a GUI using tkinter

# Import Packages needed
from tkinter import *
import tkinter.font as tkFont

# Set up root
root = Tk()
root.title("Time Worked Application")

fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=16)

outputLabel = Label(root)

# Create labels needed
label1 = Label(root, text='I help you count the time difference', font=fontStyle)
partition1 = Label(root, text='-----------------------------')
partition2 = Label(root, text='-----------------------------')

time1_label = Label(root, text='Enter start time: ', font=fontStyle2)
time2_label = Label(root, text='Enter end time: ', font=fontStyle2)

hr1_point = Label(root, text='hr ')
min1_point = Label(root, text='min ')
sec1_point = Label(root, text='sec ')

hr2_point = Label(root, text='hr ')
min2_point = Label(root, text='min ')
sec2_point = Label(root, text='sec ')

#Create a function to calculate the time
def time():
    global outputLabel
    outputLabel.destroy()

    from datetime import timedelta
    h1str = hour1_enter.get()
    h1 = int(h1str)
    min1str = min1_enter.get()
    m1 = int(min1str)
    sec1str = sec1_enter.get()
    s1 = int(sec1str)
    pm1 = t1pm.get()

    h2str = hour2_enter.get()
    h2 = int(h2str)
    min2str = min2_enter.get()
    m2 = int(min2str)
    sec2str = sec2_enter.get()
    s2 = int(sec2str)
    pm2 = t2pm.get()

    if (pm1 == 1) and (h1 != 12):
        h1 = h1+12
    if (pm1 == 0) and (h1 == 12):
        h1 = 24
    if (pm2 == 1) and (h2 != 12):
        h2 = h2+12
    if (pm2 == 0) and (h2 == 12):
        h2 = 24

    t1 = timedelta(hours=h1, minutes=m1)
    t2 = timedelta(hours=h2, minutes=m2)
    Time = t2 - t1
    outtext = 'The number of hour(s) worked is: {}'.format(Time)
    outputLabel = Label(root, text=outtext, font=fontStyle)
    outputLabel.grid(row=12, column=0)


hour1_enter = Entry(root, width=2)
hour1_enter.insert(0, "12")
min1_enter = Entry(root, width=2)
min1_enter .insert(0, "00")
sec1_enter = Entry(root, width=2)
sec1_enter .insert(0, "00")

hour2_enter = Entry(root, width=2)
hour2_enter.insert(0, "12")
min2_enter = Entry(root, width=2)
min2_enter .insert(0, "00")
sec2_enter = Entry(root, width=2)
sec2_enter .insert(0, "00")


# Create Radio Buttons
t1pm = IntVar()
t2pm = IntVar()
Radiobutton(root, text='AM', variable=t1pm, value=0).grid(row=3, column=3)
Radiobutton(root, text='PM', variable=t1pm, value=1).grid(row=4, column=3)
Radiobutton(root, text='AM', variable=t2pm, value=0).grid(row=8, column=3)
Radiobutton(root, text='PM', variable=t2pm, value=1).grid(row=9, column=3)

# Create Buttons
button1 = Button(root, text="Calculate", padx=25, pady=15, fg='red', command=time)

# Grid (Place it on to  the GUI)
label1.grid(row=0, column=1, columnspan=2)

hr1_point.grid(row=3, column=0)
min1_point.grid(row=3, column=1)
sec1_point.grid(row=3, column=2)

time1_label.grid(row=2, column=0)
hour1_enter.grid(row=4, column=0)
min1_enter.grid(row=4, column=1)
sec1_enter.grid(row=4, column=2)

partition2.grid(row=6, column=0)

time2_label.grid(row=7, column=0)

hr2_point.grid(row=8, column=0)
min2_point.grid(row=8, column=1)
sec2_point.grid(row=8, column=2)
hour2_enter.grid(row=9, column=0)
min2_enter .grid(row=9, column=1)
sec2_enter .grid(row=9, column=2)


partition1.grid(row=10, column=0)
button1.grid(row=11, column=0)


# Create an event loop (constant loop or GUI running)

root.mainloop()
