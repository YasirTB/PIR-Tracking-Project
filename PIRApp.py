# PIR Sensor Tracking Application
# Login Screen for the user followed by a screen that displays PIR Information
# User loads a txt file (output from the PIR sensors readings) to the application
# Movement is then traced on the map provided
# Its ya boy Yas 15906553 from the A to the U to the T

import sys
import os
from tkinter import ttk
from tkinter import Text
from tkinter import *
from tkinter import filedialog


def login(event):
    if entry1.get() == 'aut' and entry2.get() == 'pass':
        root.deiconify()
        top.destroy()


def cancel():
    top.destroy()
    root.destroy()
    sys.exit()


def addfile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
    label = Label(root, text=root.filename).pack()


def update(zone):
    # Single sensor zones
    if zone == 0:
        canvas.itemconfig('z0', fill='red')
    elif zone == 1:
        canvas.itemconfig('z1', fill='red')
    elif zone == 2:
        canvas.itemconfig('z2', fill='red')
    elif zone == 3:
        canvas.itemconfig('z3', fill='red')
    elif zone == 4:
        canvas.itemconfig('z4', fill='red')
    elif zone == 5:
        canvas.itemconfig('z5', fill='red')
    # Combination sensor zones
    elif zone == 1 & zone == 2:
        canvas.itemconfig('z1_2', fill='red')
    elif zone == 2 & zone == 3:
        canvas.itemconfig('z2_3', fill='red')
    elif zone == 3 & zone == 4:
        canvas.itemconfig('z3_4', fill='red')
    elif zone == 4 & zone == 5:
        canvas.itemconfig('z4_5', fill='red')
    elif zone == 5 & zone == 1:
        canvas.itemconfig('z5_1', fill='red')


# Main Screen
root = Tk()

# Frame for the main screen
frame = LabelFrame(root, padx=5, pady=5)

# Buttons on the main screen
openFile = Button(frame, text="Open File", font=('Helvetica', 10), command=addfile)
run = Button(frame, text="Execute", font=('Helvetica', 10))

hSlider = Scale(frame, from_=0, to=120, orient=HORIZONTAL)


cWidth = 800
cHeight = 650
canvas = Canvas(frame, width=cWidth, height=cHeight)

canvas.create_polygon(257, 635, 319, 445, 269, 409, 107, 526, outline='black', fill='white', tag='z1')
canvas.create_polygon(107, 526, 269, 409, 250, 350, 50, 350, outline='black', fill='white', tag='z1_2')
canvas.create_polygon(50, 350, 250, 350, 269, 291, 107, 174, outline='black', fill='white', tag='z2')
canvas.create_polygon(107, 174, 269, 291, 319, 255, 257, 65, outline='black', fill='white', tag='z2_3')
canvas.create_polygon(257, 65, 443, 65, 381, 255, 319, 255, outline='black', fill='white', tag='z3')
canvas.create_polygon(443, 65, 381, 255, 431, 291, 593, 174, outline='black', fill='white', tag='z3_4')
canvas.create_polygon(593, 174, 431, 291, 450, 350, 650, 350, outline='black', fill='white', tag='z4')
canvas.create_polygon(650, 350, 450, 350, 431, 409, 593, 526, outline='black', fill='white', tag='z4_5')
canvas.create_polygon(593, 526, 431, 409, 381, 445, 443, 635, outline='black', fill='white', tag='z5')
canvas.create_polygon(443, 635, 381, 445, 319, 445, 257, 635, outline='black', fill='white', tag='z5_1')
canvas.create_polygon(381, 255, 319, 255, 269, 291, 250, 350, 269, 409, 319, 445, 381, 445, 431, 409, 450, 350, 431,
                      291, outline='black', fill='white', tag='z0')

# Login Screen
top = Toplevel()

top.geometry('300x360')
top.title('User Login')
top.configure(background='white')
photo2 = PhotoImage(file='autlogo.png')
photo = Label(top, image=photo2, bg='white')
lbl1 = Label(top, text='Username:', font={'Helvetica', 10})
entry1 = Entry(top)
lbl2 = Label(top, text='Password:', font={'Helvetica', 10})
entry2 = Entry(top, show="*")
button2 = Button(top, text='cancel', command=lambda: cancel())
lbl3 = Label(top, text='Copyright AUT 2020 ya bish', font=('Arial', 9))

entry2.bind('<Return>', login)

# Ordering the elements
photo.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()
lbl3.pack()
frame.pack(padx=10, pady=10)
openFile.pack(padx=1, pady=1)
run.pack(padx=1, pady=1)
hSlider.pack()
canvas.pack()

root.title('main screen')
root.configure(background='white')
root.geometry('960x720')
root.withdraw()

root.mainloop()
