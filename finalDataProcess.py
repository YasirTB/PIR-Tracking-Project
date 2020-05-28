class Sensor:
    def __init__(self, id):
        self.id = id
        self.elapsedTime = 0
        self.frequency = 0

    def updateFreq(self): #Increments the frequency count by 1
        self.frequency += 1

    def updateTime(self, elapsedTime):  #Increments the elapsed time by adding the given parameter
        self.elapsedTime += elapsedTime

def preprocess(fileName):
    import pandas as pd
    df = open(fileName, "r") #Reads the txt file
    lines = df.readlines() #Creates an list of lines from the txt file
    df.close()

    for index, line in enumerate(lines): #iterate every line of the txt file
        readings = []
        #Clean up the line but removing all the spaces and separating each value based on commas
        lines[index] = line.strip()
        strToken = lines[index].replace(' -> ', '')
        strToken = strToken.split(',')

        #Slice the strToken list so that we only have the sensor readings
        sensorList = strToken[3:9]
        for data in sensorList:
            dataToken = data.split(':')
            readings.append(dataToken[1])
        readings.insert(0, strToken[0]) #Appends the time with the sensor readings
        lines[index] = readings

    #Converting the time ands sensor readings into a dataframe
    df_result = pd.DataFrame(columns=('Time', '0', '1', '2', '3', '4', '5'))
    i = 0
    for line in lines:
        df_result.loc[i] = line
        i = i + 1
    return df_result

def calculate(arr, tSensors):
    from datetime import datetime
    fullOrder = ['O']
    oldTime = 0
    currentElapsedTime = 0
    activeTime = 0
    totalTime = 0
    idle = 0
    #This for-loop iterates through the time readings and calculates the time duration between every reading
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
        for index, input in enumerate(reading): #Iterates through the 6 sensor readings and finds the readings that exceeds our thresholds
            if float(input) < 1.40 or float(input) > 2.35: # If the reading is below 1.7 or above 2.5, the sensor reads that the user is active
                tSensors[index - 1].updateFreq()
                tSensors[index - 1].updateTime(currentElapsedTime) # Accumulating the time spent in the sensor
                #Creates a string of sensors that are active
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
    # return activeTime, totalTime, fullOrder
    return fullOrder

def initSensors():
    tSensors = []
    for i in range(6):  # Instantiating 6 sensor objects
        tSensors.append(Sensor(i))
    return tSensors

def filterData(tSensors, num, type):
    lastIndex = len(tSensors)
    filtIndex = 0
    # converting numbers into seconds, multplied by 10 because it takes 10 lines for each second
    if type == 'Hours':
        filtIndex = num * 36000
    elif type == 'Minutes':
        filtIndex = num * 600
    elif type == 'Seconds':
        filtIndex = num * 10

    #If the filtering value exceeds the dataframe, no data will show up
    if filtIndex > lastIndex:
        filtIndex = 0
    firstIndex = lastIndex - filtIndex
    filteredArr = tSensors.copy()  # Copy the original dataframe
    filteredArr = filteredArr.iloc[firstIndex:lastIndex, :]  # slicing the new dataframe
    return filteredArr

def sensorStats(tSensors):
    timePerSen = []
    readPerSen = []
    for i in tSensors: #Iterates through every sensor and appends the time and read count to their respectively lists
        timePerSen.append(i.elapsedTime)
        readPerSen.append(i.frequency)
    return timePerSen,readPerSen
