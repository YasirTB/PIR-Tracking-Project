# PIR Sensor Tracking Application
# Login Screen for the user followed by a screen that displays PIR Information
# User loads a txt file (output from the PIR sensors readings) to the application
# Movement is then traced on the map provided
# Supporting Statistics are also outlined
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
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
    label = Label(tabFrame1, text=filename).pack()

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

def update(tkn, colour):
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

def select():
    selectTabs.select(1)

def runFile():
    import finalDataProcess as dp
    global sensorDF,timeData,readData,fullOrder
    tSensors = dp.initSensors()
    sensorDF = dp.preprocess(filename)
    fullOrder = dp.calculate(sensorDF,tSensors)
    timeData, readData = dp.sensorStats(tSensors)
    plotBar(timeData,readData)

def plotBar(timeD,readD):
    import tkinter as tk
    import matplotlib.pyplot as plt
    from pandas import DataFrame
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    #Clear the graphs before plotting a new one
    for widget in statsFrame.winfo_children():
        widget.destroy()

    # Creating dataframes for the readings and time data
    dTime = {'Sensor': ['0', '1', '2', '3', '4', '5'], 'Duration': timeD}
    dRead = {'Sensor': ['0', '1', '2', '3', '4', '5'], 'Count': readD}

    timeDF = DataFrame(dTime, columns=['Sensor', 'Duration'])
    readDF = DataFrame(dRead, columns=['Sensor', 'Count'])

    timeFig = plt.Figure(figsize=(4, 4), dpi=75)
    readFig = plt.Figure(figsize=(4, 4), dpi=75)

    axT = timeFig.add_subplot(111)
    barT = FigureCanvasTkAgg(timeFig, statsFrame)
    barT.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    axT.set_title('Time spent by the user on each zone')
    timeDF = timeDF[['Sensor', 'Duration']].groupby('Sensor').sum()
    timeDF.plot(kind='bar', legend=True, ax=axT)

    axR = readFig.add_subplot(111)
    barR = FigureCanvasTkAgg(readFig, statsFrame)
    barR.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    axR.set_title('Sensor read')
    readDF = readDF[['Sensor', 'Count']].groupby('Sensor').sum()
    readDF.plot(kind='bar', legend=True, ax=axR)

def filtGraph():
    import finalDataProcess as dP
    fSensors = dP.initSensors()
    filtDF = dP.filterData(sensorDF,int(fNum),fType)
    dP.calculate(filtDF, fSensors)
    timeData, readData = dP.sensorStats(fSensors)
    plotBar(timeData, readData)

def getNum(varNum):
    global fNum
    fNum = varNum

def getType(varType):
    global fType
    fType = varType

def resetGraph():
    plotBar(timeData, readData)

def runMap():
    for i in range(len(fullOrder)):
        resetMap()
        subRun(i)
        mapDelay(i)
        canvas.update()
    resetMap()

def subRun(i):
    tkn = fullOrder[i].split(',')
    canvas.after(100, update(tkn, 'red'))
def mapDelay(i):
    tknDelay2 = fullOrder[i - 1].split(',')
    tknDelay3 = fullOrder[i - 2].split(',')

    canvas.after(5, update(tknDelay2, 'red2'))
    canvas.after(10, update(tknDelay3, 'red3'))
# Main Screen
root = Tk()

# Create Tabs in App
selectTabs = ttk.Notebook()

# Setting up the Frames on the main screen
tabFrame1 = Frame(selectTabs, width=800, height=750, bg="white")
tabFrame2 = Frame(selectTabs, width=800, height=750, bg="white")

tabFrame1.pack(fill="both", expand=1)
tabFrame2.pack(fill="both", expand=1)

selectTabs.add(tabFrame1, text="Map Layout")
selectTabs.add(tabFrame2, text="Statistics")

# Frame for the Map
mapFrame = Frame(tabFrame1, height=800, width=750, borderwidth=1)
statsFrame = Frame(tabFrame2, height=800, width=750, borderwidth=1)

# Buttons on the tab 1
openFile = Button(tabFrame1, text="Open File", font=('Helvetica', 10), command=addfile)
run = Button(tabFrame1, text="Execute", font=('Helvetica', 10), command=runFile)
playButton = Button(tabFrame1, text="Play", font=('Helvetica', 10), command = runMap)
stopButton = Button(tabFrame1, text="Stop", font=('Helvetica', 10), command=resetMap)

# Navigate to the Stat Tab
navigateStat = Button(tabFrame1, text="Show Stats", command=select)

clicked = StringVar()
clicked.set("Select Time Unit")

hSlider = Scale(tabFrame2, from_= 0, to=60, orient=HORIZONTAL,command = getNum)
dropMenu = OptionMenu(tabFrame2, clicked, "Hours", "Minutes", "Seconds", command=getType)

filterButton = Button(tabFrame2, text = 'Filter',command = filtGraph)
resetGButton = Button(tabFrame2, text = 'Reset',command = resetGraph)

cWidth = 660
cHeight = 600
global canvas
canvas = Canvas(mapFrame, width=cWidth, height=cHeight)

# Outer Zones
zn1 = canvas.create_polygon(276, 578, 325, 426, 285, 397, 156, 491, outline='black', fill='white', tag='z1')
zn12 = canvas.create_polygon(285, 397, 270, 350, 110, 350, 156, 491, outline='black', fill='white', tag='z1_2')
zn2 = canvas.create_polygon(110, 350, 270, 350, 285, 303, 156, 209, outline='black', fill='white', tag='z2')
zn23 = canvas.create_polygon(285, 303, 325, 274, 276, 122, 156, 209, outline='black', fill='white', tag='z2_3', )
zn3 = canvas.create_polygon(424, 122, 276, 122, 325, 274, 375, 274, outline='black', fill='white', tag='z3')
zn34 = canvas.create_polygon(424, 122, 375, 274, 415, 303, 544, 209, outline='black', fill='white', tag='z3_4')
zn4 = canvas.create_polygon(544, 209, 415, 303, 430, 350, 590, 350, outline='black', fill='white', tag='z4')
zn45 = canvas.create_polygon(590, 350, 430, 350, 415, 397, 544, 491, outline='black', fill='white', tag='z4_5')
zn5 = canvas.create_polygon(544, 491, 415, 397, 375, 426, 424, 578, outline='black', fill='white', tag='z5')
zn51 = canvas.create_polygon(424, 578, 375, 426, 325, 426, 276, 578, outline='black', fill='white', tag='z5_1')

# Inner Zones
zn1I = canvas.create_polygon(325, 426, 285, 397, 350, 350, outline='black', fill='white', tag='z1I')
zn12I = canvas.create_polygon(285, 397, 270, 350, 350, 350, outline='black', fill='white', tag='z1_2I')
zn2I = canvas.create_polygon(270, 350, 285, 303, 350, 350, outline='black', fill='white', tag='z2I')
zn23I = canvas.create_polygon(285, 303, 325, 274, 350, 350, outline='black', fill='white', tag='z2_3I', )
zn3I = canvas.create_polygon(325, 274, 375, 274, 350, 350, outline='black', fill='white', tag='z3I')
zn34I = canvas.create_polygon(375, 274, 415, 303, 350, 350, outline='black', fill='white', tag='z3_4I')
zn4I = canvas.create_polygon(430, 350, 415, 303, 350, 350, outline='black', fill='white', tag='z4I')
zn45I = canvas.create_polygon(430, 350, 415, 397, 350, 350, outline='black', fill='white', tag='z4_5I')
zn5I = canvas.create_polygon(415, 397, 375, 426, 350, 350, outline='black', fill='white', tag='z5I')
zn51I = canvas.create_polygon(325, 426, 375, 426, 350, 350, outline='black', fill='white', tag='z5_1I')

# Zone labels
zn1_label = Label(canvas, text='Zone 1', fg='black', bg='white')
zn12_label = Label(canvas, text='Zone 1 & 2', fg='black', bg='white')
zn2_label = Label(canvas, text='Zone 2', fg='black', bg='white')
zn23_label = Label(canvas, text='Zone 2 & 3', fg='black', bg='white')
zn3_label = Label(canvas, text='Zone 3', fg='black', bg='white')
zn34_label = Label(canvas, text='Zone 3 & 4', fg='black', bg='white')
zn4_label = Label(canvas, text='Zone 4', fg='black', bg='white')
zn45_label = Label(canvas, text='Zone 4 & 5', fg='black', bg='white')
zn5_label = Label(canvas, text='Zone 5', fg='black', bg='white')
zn51_label = Label(canvas, text='Zone 5 & 1', fg='black', bg='white')

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

###STATS
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
timeFig = plt.Figure(figsize=(4, 4), dpi=75)
readFig = plt.Figure(figsize=(4, 4), dpi=75)
axT = timeFig.add_subplot(111)
barT = FigureCanvasTkAgg(timeFig, statsFrame)
barT.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
axT.set_title('Time spent by the user on each zone')

axR = readFig.add_subplot(111)
barR = FigureCanvasTkAgg(readFig, statsFrame)
barR.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
axR.set_title('Sensor read')



# Login Screen Config
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
selectTabs.pack()
mapFrame.pack()
statsFrame.pack()
hSlider.pack()
dropMenu.pack()
canvas.pack()
openFile.pack()
run.pack()
# navigateStat.pack()
filterButton.pack()
resetGButton.pack()
playButton.pack()
# stopButton.pack()
root.title('main screen')
root.configure(background='white')
root.geometry('660x720')
root.withdraw()

root.mainloop()
