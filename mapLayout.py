from tkinter import *
import time
root = Tk()
cWidth = 800
cHeight = 650
canvas = Canvas(root, width=cWidth, height=cHeight)
canvas.pack()

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
zn0 = canvas.create_polygon(375,274,325,274,285,303,270,350,285,397,325,426,375,426,415,397,430,350,415,303,outline='orange',fill='white', tag='z0')


# Zone labels
zn0_label = Label(canvas, text='Zone 0', fg='black', bg='white')
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

canvas.create_window(350,350, window=zn0_label)
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
    #root.update()
    root.after(100,task,i+1) # call this function per 0.1 second

root.after(100,task,index) # call after function and pass a index argument
root.mainloop()
