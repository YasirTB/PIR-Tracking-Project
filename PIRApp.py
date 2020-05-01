# PIR Sensor Tracking Application
# Login Screen for the user followed by a screen that displays PIR Information
# User loads a txt file (output from the PIR sensors readings) to the application
# Movement is then traced on the map provided
# Its ya boy Yas 15906553 from the A to the U to the T

from tkinter import *
from tkinter import filedialog, ttk
import sys
import time


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
    label = Label(tabFrame1, text=root.filename).pack()


def resetMap():
    canvas.itemconfig(zn0, fill='white')
    canvas.itemconfig(zn1, fill='white')
    canvas.itemconfig(zn12, fill='white')
    canvas.itemconfig(zn2, fill='white')
    canvas.itemconfig(zn23, fill='white')
    canvas.itemconfig(zn3, fill='white')
    canvas.itemconfig(zn34, fill='white')
    canvas.itemconfig(zn4, fill='white')
    canvas.itemconfig(zn45, fill='white')
    canvas.itemconfig(zn5, fill='white')
    canvas.itemconfig(zn51, fill='white')


def update(tkn):
    if len(tkn) == 1:
        if '0' in tkn:
            canvas.itemconfig(zn0, fill='red')
        elif '1' in tkn:
            canvas.itemconfig(zn1, fill='red')
        elif '2' in tkn:
            canvas.itemconfig(zn2, fill='red')
        elif '3' in tkn:
            canvas.itemconfig(zn3, fill='red')
        elif '4' in tkn:
            canvas.itemconfig(zn4, fill='red')
        elif '5' in tkn:
            canvas.itemconfig(zn5, fill='red')
    else:
        # run combination
        if '0' in tkn:
            canvas.itemconfig(zn0, fill='red')
        elif '1' in tkn and '2' in tkn:
            canvas.itemconfig(zn12, fill='red')
        elif '2' in tkn and '3' in tkn:
            canvas.itemconfig(zn23, fill='red')
        elif '3' in tkn and '4' in tkn:
            canvas.itemconfig(zn34, fill='red')
        elif '4' in tkn and '5' in tkn:
            canvas.itemconfig(zn45, fill='red')
        elif '5' in tkn and '1' in tkn:
            canvas.itemconfig(zn51, fill='red')


index = 0


def task(i):
    if i == len(L):  # check whether the index larger than the length of the list.
        return
    resetMap()
    tkn = L[i].split('_')
    update(tkn)
    root.update()
    root.after(100, task, i + 1)  # call this function per 0.1 second
    root.after(100, task, index)  # call after function and pass a index argument


def select():
    selectTabs.select(1)


# Main Screen
root = Tk()

# Frame for the main screen
# frame = LabelFrame(root, padx=5, pady=5)

# Create Tabs in App
selectTabs = ttk.Notebook()

tabFrame1 = Frame(selectTabs, width=800, height=750, bg="white")
tabFrame2 = Frame(selectTabs, width=800, height=750, bg="white")

tabFrame1.pack(fill="both", expand=1)
tabFrame2.pack(fill="both", expand=1)

selectTabs.add(tabFrame1, text="Map Layout")
selectTabs.add(tabFrame2, text="Statistics")

# Buttons on the tab 1
openFile = Button(tabFrame1, text="Open File", font=('Roboto', 10), command=addfile)
run = Button(tabFrame1, text="Execute", font=('Roboto', 10))

# Navigate to the Stat Tab
navigateStat = Button(tabFrame1, text="Show Stats", command=select)

clicked = StringVar()
clicked.set("Select Time Unit")

hSlider = Scale(tabFrame2, from_=0, to=120, orient=HORIZONTAL)
dropMenu = OptionMenu(tabFrame2, clicked, "Hours", "Minutes", "Seconds")

cWidth = 800
cHeight = 650
canvas = Canvas(tabFrame1, width=cWidth, height=cHeight)

zn23 = canvas.create_polygon(285, 303, 325, 274, 276, 122, 156, 209, outline='blue', fill='white', tag='z2_3')
zn2 = canvas.create_polygon(110, 350, 270, 350, 285, 303, 156, 209, outline='black', fill='white', tag='z2')
zn12 = canvas.create_polygon(285, 397, 270, 350, 110, 350, 156, 491, outline='purple', fill='white', tag='z1_2')
zn1 = canvas.create_polygon(276, 578, 325, 426, 285, 397, 156, 491, outline='black', fill='white', tag='z1')
zn51 = canvas.create_polygon(424, 578, 375, 426, 325, 426, 276, 578, outline='orange', fill='white', tag='z5_1')
zn5 = canvas.create_polygon(544, 491, 415, 397, 375, 426, 424, 578, outline='black', fill='white', tag='z5')
zn45 = canvas.create_polygon(590, 350, 430, 350, 415, 397, 544, 491, outline='cyan', fill='white', tag='z4_5')
zn4 = canvas.create_polygon(544, 209, 415, 303, 430, 350, 590, 350, outline='black', fill='white', tag='z4')
zn34 = canvas.create_polygon(424, 122, 375, 274, 415, 303, 544, 209, outline='green', fill='white', tag='z3_4')
zn3 = canvas.create_polygon(424, 122, 276, 122, 325, 274, 375, 274, outline='black', fill='white', tag='z3')
zn0 = canvas.create_polygon(375, 274, 325, 274, 285, 303, 270, 350, 285, 397, 325, 426, 375, 426, 415, 397, 430, 350,
                            415, 303, outline='black', fill='white', tag='z0')

L = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
     '5', '5', '1_5', '1_5', '5', '5', '5', '5', '5', '5', '5', '5', '1', '1', '1', '1', '1', '1', '1_5', '5', '1',
     '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1_2', '2', '1_2', '0_1', '0_1', '0_1', '0_1', '1', '1',
     '0_1', '0', '0_1_2', '1_2', '1', '1_2', '2', '2', '2', '2', '2', '2', '2', '1', '1', '2', '2', '2', '2_3',
     '2_3', '0_2_3', '0_2', '0_2', '0_2', '2', '2', '2', '2_3', '3', '2_3', '2', '2_3', '2_3_4', '3_4', '3', '3',
     '3_4', '3_4', '2_3_4', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3',
     '3', '4', '3', '3', '3_4', '4', '4', '4', '4', '3_4', '4', '4', '0_3_4', '3_4', '3', '3', '3', '3', '0', '4',
     '0_4', '4', '4', '5', '4', '4', '4', '4', '4_5', '4_5', '4_5', '4_5', '5', '5', '5', '5', '5', '5', '0_5',
     '0_5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
     '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
     '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '1_5', '5', '5', '5', '1',
     '1_5', '0_5', '0', '0', '0', '0_1_5', '0_5', '0_5', '0_1', '0_1', '0', '1', '1_2', '0_2', '0_1', '0_1', '0_1',
     '2', '1_2', '1', '0_1_2', '0_1_2', '0_1_2', '1_3', '3', '0', '0_2', '2', '2', '0', '0_2', '2', '2', '0_3',
     '0_3', '0_3', '0', '0', '0', '0', '0', '3_4', '0_3_4', '0_3_4', '0', '0', '4', '5', '5', '0', '4_5', '4_5',
     '4_5', '4', '4', '4', '4', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
     '5', '5', '1']

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
# frame.pack(padx=10, pady=10)
selectTabs.pack()
hSlider.pack()
dropMenu.pack()
canvas.pack()
openFile.pack()
run.pack()
navigateStat.pack(pady=10)

root.title('main screen')
root.configure(background='white')
root.geometry('800x800')
root.withdraw()

root.mainloop()
