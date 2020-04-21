from tkinter import *
import time
root = Tk()
cWidth = 800
cHeight = 650
canvas = Canvas(root, width=cWidth, height=cHeight)
canvas.pack()

zn1 = canvas.create_polygon(257, 635, 319, 445, 269, 409, 107, 526,outline='blue',fill='white',tag='z1',)
zn12 = canvas.create_polygon(107, 526, 269, 409, 250, 350, 50, 350,outline='black',fill='white', tag='z1_2')
zn2 = canvas.create_polygon(50, 350, 250, 350, 269, 291, 107, 174,outline='purple',fill='white', tag='z2')
zn23 = canvas.create_polygon(107, 174, 269, 291, 319, 255, 257, 65,outline='black',fill='white', tag='z2_3')
zn3 = canvas.create_polygon(257, 65, 443, 65, 381, 255, 319, 255,outline='orange',fill='white', tag='z3')
zn34 = canvas.create_polygon(443, 65, 381, 255, 431, 291, 593, 174,outline='black',fill='white', tag='z3_4')
zn4 = canvas.create_polygon(593, 174, 431, 291, 450, 350, 650, 350,outline='cyan',fill='white', tag='z4')
zn45 = canvas.create_polygon(650, 350, 450, 350, 431, 409, 593, 526,outline='black',fill='white', tag='z4_5')
zn5 = canvas.create_polygon(593, 526, 431, 409, 381, 445, 443, 635,outline='green',fill='white', tag='z5')
zn51 = canvas.create_polygon(443, 635, 381, 445, 319, 445, 257, 635,outline='black',fill='white', tag='z5_1')
zn0 = canvas.create_polygon(381, 255, 319, 255, 269, 291, 250, 350, 269, 409, 319, 445, 381, 445, 431, 409, 450, 350,
                            431, 291,outline='black',fill='white', tag='z0')

L= ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5',
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
    if i == len(L): # check whether the index larger than the length of the list.
        return
    resetMap()
    tkn = L[i].split('_')
    update(tkn)
    root.update()
    root.after(100,task,i+1) # call this function per 0.1 second

root.after(100,task,index) # call after function and pass a index argument
root.mainloop()
