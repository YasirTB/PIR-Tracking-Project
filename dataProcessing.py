import numpy

class Sensor:
    def __init__(self, id):
        self.id = id
        self.elapsedTime = 0
        self.frequency = 0

    def updateFreq(self):
        self.frequency += 1

    def updateTime(self, elapsedTime):
        self.elapsedTime += elapsedTime

def preprocess(fileName):
    import pandas as pd
    df = open(fileName, "r")
    lines = df.readlines()
    df.close()

    for index, line in enumerate(lines):
        readings = []
        lines[index] = line.strip()
        strToken = lines[index].replace(' -> ', '')
        strToken = strToken.split(',')
        sensorList = strToken[3:9]
        for data in sensorList:
            dataToken = data.split(':')
            readings.append(dataToken[1])
        readings.insert(0, strToken[0])
        lines[index] = readings

    df_result = pd.DataFrame(columns=('Time', '0', '1', '2', '3', '4', '5'))
    i = 0
    for line in lines:
        df_result.loc[i] = line
        i = i + 1
   # print(df_result)
    return df_result

def filterData(tSensors, num):
    #from the original dataframe, slice the dataframe into a new dataframe
    #num is the user input in sec, e.g last 10,20,30 sec
    #It takes 10 lines of output for 1 sec

    #eg old df = 30sec=300lines
    #user wants to see the last 10 sec
    # 10 lines * 10 secs = 100 lines
    #range is 200 to 300 the (last 10 sec)
    # copy the last 100 lines of the old dataframe into a new dataframe
    lastIndex = len(tSensors)
    firstIndex= lastIndex - (num*10)
    filteredArr = tSensors.copy() #Slice the dataframe
    filteredArr=filteredArr.iloc[firstIndex:lastIndex,:]
    return filteredArr

def sensorStats(tSensors):
    #tSensors is an array list of the 6 sensors
    #function will give two array list, time duration and sensor freq for every sensor
    #useful for graphs
    timePerSen = []
    readPerSen = []
    for i in tSensors:
        timePerSen.append(i.elapsedTime)
        readPerSen.append(i.frequency)
    return timePerSen,readPerSen

def calculate(arr, tSensors):
    from datetime import datetime
    fullOrder = ['O']
    oldTime = 0
    currentElapsedTime = 0
    activeTime = 0
    totalTime = 0
    idle = 0
    for index, line in arr.iterrows():
        fmt = '%H:%M:%S.%f'
        time = datetime.strptime(line[0], fmt)
        if (oldTime == 0):
            oldTime = float(time.hour) * 3600 + float(time.minute) * 60 + float(time.second) + float(
                time.microsecond) / 1e6
        else:
            newTime = float(time.hour) * 3600 + float(time.minute) * 60 + float(time.second) + float(
                time.microsecond) / 1e6
            currentElapsedTime = (newTime - oldTime)
            oldTime = newTime
        totalTime += currentElapsedTime # Adding current time duration to the total time duration
        reading = line[1:7] # Slicing the data for the sensor readings into a new list
        order = ''
        for index, input in enumerate(reading): #Iterates through the 6 sensor readings
            if float(input) < 1.7 or float(input) > 2.5: # If the reading is below 1.7 or above 2.5, the sensor reads that the user is active
                tSensors[index - 1].updateFreq()
                tSensors[index - 1].updateTime(currentElapsedTime) # Accumulating the time spent in the sensor
                if len(order) == 0:
                    order += str(index)
                else:
                    order += ',' + str(index)
        if len(order) == 1:
            fullOrder.append(order)
            activeTime += currentElapsedTime
        elif len(order) > 1:
            fullOrder.append(order)
            activeTime += currentElapsedTime
        else:
            fullOrder.append(fullOrder[len(fullOrder)-1])
            idle += currentElapsedTime
    print(activeTime,idle,activeTime+idle)
    return activeTime, totalTime, fullOrder

def initSensors():
    tSensors = []
    for i in range(6):  # Instantiating 6 sensor objects
        tSensors.append(Sensor(i))
    return tSensors

def summary(sensors):
    totalFreq = 0
    for i in sensors:
        print('The user has been in zone', round(i.frequency, 2), 'times for', round(i.elapsedTime, 2),
              'seconds.')
        totalFreq += i.frequency
    return totalFreq

def main():
    preArray = preprocess("C:/Users/Miguel/OneDrive/AUT/Final Year Project/data/tommy_inout.txt")
    Sensors = initSensors()
    active, total, fullOrder = calculate(preArray, Sensors)
    # print('The user has been active for', round(active, 2), 'seconds within a time duration of', round(total, 2),
    #       'seconds')
    # tFreq = summary(Sensors)
    # for i in Sensors:
    #     print('Sensor',i.id,round((i.frequency/tFreq)*100,2), '%', i.elapsedTime,'sec',i.frequency,'times')
    g1,g2 = sensorStats(Sensors)
    print(preArray, g1, g2)

    ##Filtered
    filtSen = initSensors()
    filtData = filterData(preArray,10)
    #filtStats
    calculate(filtData,filtSen)
    d1, d2 = sensorStats(filtSen)
    print(filtData,d1,d2)


main()
