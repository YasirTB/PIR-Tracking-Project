#Two arrays should be passed into the timeData and readData
timeData = [6.440999999998894, 4.2480000000068685, 5.1990000000078, 3.577999999994063, 4.55899999999383, 5.197000000000116]
readData = [64, 42, 51, 35, 45, 51]

import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dTime = {'Sensor':['0','1', '2','3','4','5'],'Duration': timeData}
dRead = {'Sensor': ['0', '1', '2', '3', '4', '5'], 'Count': readData}

timeDF = DataFrame(dTime,columns=['Sensor','Duration'])
readDF = DataFrame(dRead,columns=['Sensor','Count'])

root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
timeDF = timeDF[['Sensor','Duration']].groupby('Sensor').sum()
timeDF.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Time spent by the user on each zone')

figure2 = plt.Figure(figsize=(6, 5), dpi=100)
ax2 = figure2.add_subplot(111)
bar2 = FigureCanvasTkAgg(figure2, root)
bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
readDF = readDF[['Sensor','Count']].groupby('Sensor').sum()
readDF.plot(kind='bar', legend=True, ax=ax2)
ax2.set_title('Sensor read')

root.mainloop()