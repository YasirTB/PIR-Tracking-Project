def plotBar(timeData, readData):
    import tkinter as tk
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    #Creating dataframes for the readings and time data
    dTime = {'Sensor': ['0', '1', '2', '3', '4', '5'], 'Duration': timeData}
    dRead = {'Sensor': ['0', '1', '2', '3', '4', '5'], 'Count': readData}

    timeDF = DataFrame(dTime, columns=['Sensor', 'Duration'])
    readDF = DataFrame(dRead, columns=['Sensor', 'Count'])

    root = tk.Tk()

    figure1 = plt.Figure(figsize=(5, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    timeDF = timeDF[['Sensor', 'Duration']].groupby('Sensor').sum()
    timeDF.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Time spent by the user on each zone')

    figure2 = plt.Figure(figsize=(5, 5), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, root)
    bar2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    readDF = readDF[['Sensor', 'Count']].groupby('Sensor').sum()
    readDF.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_title('Sensor read')

    root.mainloop()

def filterData(tSensors, num, type):
    lastIndex = len(tSensors)
    filtIndex = 0
    #converting numbers into seconds, multplied by 10 because it takes 10lines for each second
    if type == 'Hours':
        filtIndex = num * 36000
    elif type == 'Minutes':
        filtIndex = num * 600
    elif type == 'Seconds':
        filtIndex = num * 10

    if filtIndex > lastIndex:
        filtIndex = 0
        
    firstIndex = lastIndex - filtIndex
    filteredArr = tSensors.copy() #Copy the original dataframe
    filteredArr=filteredArr.iloc[firstIndex:lastIndex,:] #slicing the new dataframe
    return filteredArr

def sensorStats(tSensors):
    timePerSen = []
    readPerSen = []
    #Appends time and readings for each sensor into separate arrays
    for i in tSensors:
        timePerSen.append(i.elapsedTime)
        readPerSen.append(i.frequency)
    return timePerSen,readPerSen
