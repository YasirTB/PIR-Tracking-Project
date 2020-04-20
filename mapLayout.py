from tkinter import *
root = Tk()
cWidth = 800
cHeight = 650
canvas = Canvas(root, width=cWidth, height=cHeight)
canvas.pack()

canvas.create_polygon(257, 635, 319, 445, 269, 409, 107, 526,outline='black',fill='white', tag='z1')
canvas.create_polygon(107, 526, 269, 409, 250, 350, 50, 350,outline='black',fill='white', tag='z1_2')
canvas.create_polygon(50, 350, 250, 350, 269, 291, 107, 174,outline='black',fill='white', tag='z2')
canvas.create_polygon(107, 174, 269, 291, 319, 255, 257, 65,outline='black',fill='white', tag='z2_3')
canvas.create_polygon(257, 65, 443, 65, 381, 255, 319, 255,outline='black',fill='white', tag='z3')
canvas.create_polygon(443, 65, 381, 255, 431, 291, 593, 174,outline='black',fill='white', tag='z3_4')
canvas.create_polygon(593, 174, 431, 291, 450, 350, 650, 350,outline='black',fill='white', tag='z4')
canvas.create_polygon(650, 350, 450, 350, 431, 409, 593, 526,outline='black',fill='white', tag='z4_5')
canvas.create_polygon(593, 526, 431, 409, 381, 445, 443, 635,outline='black',fill='white', tag='z5')
canvas.create_polygon(443, 635, 381, 445, 319, 445, 257, 635,outline='black',fill='white', tag='z5_1')
canvas.create_polygon(381, 255, 319, 255, 269, 291, 250, 350, 269, 409, 319, 445, 381, 445, 431, 409, 450, 350, 431, 291,outline='black',fill='white', tag='z0')


def update(zone):
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

root.mainloop()