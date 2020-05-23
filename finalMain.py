#from mapProcess import *
from finalDataProcess import *
from finalGraphStats import *
def main():
    preArray=preprocess("C:/Users/Miguel/OneDrive/AUT/Final Year Project/data/tommy_inout.txt")
    Sensors = initSensors()
    active, total, fullOrder = calculate(preArray, Sensors)
    g1, g2 = sensorStats(Sensors)
    plotBar(g1, g2)

main()