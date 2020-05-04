from tkinter import *
import time

root = Tk()
cWidth = 800
cHeight = 650
canvas = Canvas(root, width=cWidth, height=cHeight)
canvas.pack()

#Outer Zones
zn1 = canvas.create_polygon(276,578,325,426,285,397,156,491,outline='black',fill='white', tag='z1')
zn12 = canvas.create_polygon(285,397,270,350,110,350,156,491,outline='black',fill='white', tag='z1_2')
zn2 = canvas.create_polygon(110,350,270,350,285,303,156,209,outline='black',fill='white', tag='z2')
zn23 = canvas.create_polygon(285,303,325,274,276,122,156,209,outline='black',fill='white',tag='z2_3',)
zn3 = canvas.create_polygon(424,122,276,122,325,274,375,274,outline='black',fill='white', tag='z3')
zn34 = canvas.create_polygon(424,122,375,274,415,303,544,209,outline='black',fill='white', tag='z3_4')
zn4 = canvas.create_polygon(544,209,415,303,430,350,590,350,outline='black',fill='white', tag='z4')
zn45 = canvas.create_polygon(590,350,430,350,415,397,544,491,outline='black',fill='white', tag='z4_5')
zn5 = canvas.create_polygon(544,491,415,397,375,426,424,578,outline='black',fill='white', tag='z5')
zn51 = canvas.create_polygon(424,578,375,426,325,426,276,578,outline='black',fill='white', tag='z5_1')

#Inner Zones
zn1I = canvas.create_polygon(325,426,285,397,350,350,outline='black',fill='white', tag='z1I')
zn12I = canvas.create_polygon(285,397,270,350,350,350,outline='black',fill='white', tag='z1_2I')
zn2I = canvas.create_polygon(270,350,285,303,350,350,outline='black',fill='white', tag='z2I')
zn23I = canvas.create_polygon(285,303,325,274,350,350,outline='black',fill='white',tag='z2_3I',)
zn3I = canvas.create_polygon(325,274,375,274,350,350,outline='black',fill='white', tag='z3I')
zn34I = canvas.create_polygon(375,274,415,303,350,350,outline='black',fill='white', tag='z3_4I')
zn4I = canvas.create_polygon(430,350,415,303,350,350,outline='black',fill='white', tag='z4I')
zn45I = canvas.create_polygon(430,350,415,397,350,350,outline='black',fill='white', tag='z4_5I')
zn5I = canvas.create_polygon(415,397,375,426,350,350,outline='black',fill='white', tag='z5I')
zn51I = canvas.create_polygon(325,426,375,426,350,350,outline='black',fill='white', tag='z5_1I')

# Zone labels
zn1_label = Label(canvas, text='Zone 1', fg='black', bg='white')
zn12_label = Label(canvas, text='Zone 1&2', fg='black', bg='white')
zn2_label = Label(canvas, text='Zone 2', fg='black', bg='white')
zn23_label = Label(canvas, text='Zone 2&3', fg='black', bg='white')
zn3_label = Label(canvas, text='Zone 3', fg='black', bg='white')
zn34_label = Label(canvas, text='Zone 3&4', fg='black', bg='white')
zn4_label = Label(canvas, text='Zone 4', fg='black', bg='white')
zn45_label = Label(canvas, text='Zone 4&5', fg='black', bg='white')
zn5_label = Label(canvas, text='Zone 5', fg='black', bg='white')
zn51_label = Label(canvas, text='Zone 5&1', fg='black', bg='white')

canvas.create_window(200, 400, window=zn1_label)
canvas.create_window(200, 310, window=zn12_label)
canvas.create_window(250, 225, window=zn2_label)
canvas.create_window(350, 200, window=zn23_label)
canvas.create_window(450, 225, window=zn3_label)
canvas.create_window(500, 310, window=zn34_label)
canvas.create_window(500, 400, window=zn4_label)
canvas.create_window(450, 475, window=zn45_label)
canvas.create_window(350, 500, window=zn5_label)
canvas.create_window(250, 475, window=zn51_label)

L= ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '1', '1', '1', '1', '1', '1', '1', '1,5', '1,5', '1,5', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0,1', '0,1', '0,1', '0,1', '1', '0,1,2', '0,1', '0', '1,2', '1,2', '1', '1,2', '1,2', '2', '2', '2', '1,2', '1,2', '0,1,2', '0,2', '0,2', '2', '0,1,2', '0,1,2', '0,1', '2', '2', '0,2,3', '0,2,3', '3', '2', '2,3', '3', '3', '3', '3', '3,4', '3', '3', '3', '3', '3', '3', '3', '3', '3', '2', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3,4', '3,4', '4', '4', '4', '4', '0,3,4', '0,3,4', '3', '3', '3', '0', '0', '0,4,5', '4,5', '4', '5', '4,5', '4', '4', '4', '4', '4', '4,5', '4,5', '4,5', '5', '5', '5', '5', '5', '5', '0,5', '0,5', '0', '5', '5', '5', '5', '5', '5', '5', '1', '1,5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '5', '1', '1', '1', '1,5', '1,5', '1,5', '0,1,2', '0,5', '1,2,5', '0,1,2', '0,1,2', '1', '1,2', '0,2', '0,2', '2', '2', '1,2', '1', '1,2', '2', '2', '1,2,3', '1,2,3', '0,1', '0,3', '0,2,3', '2', '0,3,4', '0,2,3,4', '0,2,3', '2', '0,3', '0,1,3,4', '1,3,4', '1', '0,1,3,4', '0,1,3,4', '1', '1,2,3', '0,3,4', '0', '3,4', '0,3,4', '0,3,4', '0,5', '3,4,5', '4', '4', '3,5', '3,4,5', '3,4', '5', '3,4,5', '4', '4', '5', '4,5', '4,5', '0', '0', '0,5', '5', '0,1', '0,1', '0,1', '1', '1', '0,5', '0,5', '0,5', '0,5', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']


def resetMap():
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

    canvas.itemconfig(zn1I, fill='white')
    canvas.itemconfig(zn12I, fill='white')
    canvas.itemconfig(zn2I, fill='white')
    canvas.itemconfig(zn23I, fill='white')
    canvas.itemconfig(zn3I, fill='white')
    canvas.itemconfig(zn34I, fill='white')
    canvas.itemconfig(zn4I, fill='white')
    canvas.itemconfig(zn45I, fill='white')
    canvas.itemconfig(zn5I, fill='white')
    canvas.itemconfig(zn51I, fill='white')

def update(tkn,colour):
    if len(tkn) == 1:
        if '1' in tkn:
            canvas.itemconfig(zn1, outline='black', fill=colour)
        elif '2' in tkn:
            canvas.itemconfig(zn2, outline='black', fill=colour)
        elif '3' in tkn:
            canvas.itemconfig(zn3, outline='black', fill=colour)
        elif '4' in tkn:
            canvas.itemconfig(zn4, outline='black', fill=colour)
        elif '5' in tkn:
            canvas.itemconfig(zn5, outline='black', fill=colour)
    elif len(tkn) == 2:
        if '1' in tkn and '2' in tkn:
            canvas.itemconfig(zn12, outline='black', fill=colour)
        elif '2' in tkn and '3' in tkn:
            canvas.itemconfig(zn23, outline='black', fill=colour)
        elif '3' in tkn and '4' in tkn:
            canvas.itemconfig(zn34, outline='black', fill=colour)
        elif '4' in tkn and '5' in tkn:
            canvas.itemconfig(zn45, outline='black', fill=colour)
        elif '5' in tkn and '1' in tkn:
            canvas.itemconfig(zn51, outline='black', fill=colour)
        elif '0' in tkn and '1' in tkn:
            canvas.itemconfig(zn1I, outline='black', fill=colour)
        elif '0' in tkn and '2' in tkn:
            canvas.itemconfig(zn2I, outline='black', fill=colour)
        elif '0' in tkn and '3' in tkn:
            canvas.itemconfig(zn3I, outline='black', fill=colour)
        elif '0' in tkn and '4' in tkn:
            canvas.itemconfig(zn4I, outline='black', fill=colour)
        elif '0' in tkn and '5' in tkn:
            canvas.itemconfig(zn5I, outline='black', fill=colour)
    else:
        if '0' in tkn:
            if '1' in tkn and '2' in tkn:
                canvas.itemconfig(zn12I, outline='black', fill=colour)
            elif '2' in tkn and '3' in tkn:
                canvas.itemconfig(zn23I, outline='black', fill=colour)
            elif '3' in tkn and '4' in tkn:
                canvas.itemconfig(zn34I, outline='black', fill=colour)
            elif '4' in tkn and '5' in tkn:
                canvas.itemconfig(zn45I, outline='black', fill=colour)
            elif '5' in tkn and '1' in tkn:
                canvas.itemconfig(zn51I, outline='black', fill=colour)
index = 0

def task(i):
    if i == len(L): # check whether the index larger than the length of the list.
        return
    resetMap()

    tkn = L[i].split(',')
    update(tkn,'red')

    #Fade effects
    tknDelay2 = L[i - 1].split(',')
    tknDelay3 = L[i - 2].split(',')
    root.after(5,update(tknDelay2,'red2'))
    root.after(10, update(tknDelay3, 'red3'))

    root.update()
    root.after(100,task,i+1) # call this function per 0.3 second

root.after(100,task,index) # call after function and pass a index argument
root.mainloop()
