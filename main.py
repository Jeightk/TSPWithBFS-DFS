import util
import math

xArray = []
yArray = []

positions = []



#create each independent position variable with given data.  xArray.length == yArray.length MUST!
def setPositions():
    util.readFile()

    xArray = util.getxArray()
    yArray = util.getyArray()


    for x in range(len(xArray)):
        #create dictionary obj & add to position list
        if x == 0: # 1
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [1,2,3], spot = 0)
        elif x == 1: # 2
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [2], spot = 1)
        elif x == 2: # 3
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [3,4], spot = 2)
        elif x == 3: # 4
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [4,5,6], spot = 3)
        elif x == 4: # 5
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [6, 7], spot = 4)
        elif x == 5: # 6
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [7], spot = 5)
        elif x == 6: # 7
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [8,9], spot = 6)
        elif x == 7: #8
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [8,9,10], spot = 7)
        elif x == 8: #9
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [10], spot = 8)
        elif x == 9: # 10 
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [10], spot = 9)
        elif x == 10: # 11 the end
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [], spot = 10)

        
        positions.append(pos)

    print(xArray)
    print(yArray)

def evalDistanceBFS(posi):

    connectedToArray = posi['connectedTo']

    if len(connectedToArray) == 0:
        return 0

    xValuep1 = posi['xValue']
    yValuep1 = posi['yValue']
    distanceVals = []
    connectPositions = []
    for x in range(len(connectedToArray)):
        val = connectedToArray[x]

        tempVal = positions[val]

        xValuep2 = tempVal['xValue']
        yValuep2 = tempVal['yValue']
        dist = math.sqrt((xValuep2 - xValuep1)**2 + (yValuep2 - yValuep1)**2)
        distanceVals.append(dist)
        connectPositions.append(tempVal)

    #print("vals: ", posi['connectedTo'])
    index = distanceVals.index(min(distanceVals))
    print("Min Distance: ", min(distanceVals))
    nextPosi = connectPositions[index]
    print(posi['spot'], " to ", nextPosi['spot'])

    evalDistanceBFS(nextPosi)

    #print(distanceVals)
    #print(connectPositions)

    #find distance between both pos's
    #dist = math.sqrt((xValuep2 - xValuep1)**2 + (yValuep2 - yValuep1)**2)


if __name__ == "__main__":
    setPositions()
    evalDistanceBFS(positions[0])