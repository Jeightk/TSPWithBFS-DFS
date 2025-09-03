import util


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
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [1,2,3])
        elif x == 1: # 2
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [2])
        elif x == 2: # 3
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [3,4])
        elif x == 3: # 4
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [4,5,6])
        elif x == 4: # 5
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [6, 7])
        elif x == 5: # 6
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [7])
        elif x == 6: # 7
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [8,9])
        elif x == 7: #8
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [8,9,10])
        elif x == 8: #9
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [10])
        elif x == 9: # 10 
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [10])
        elif x == 10: # 11 the end
            pos = dict(xValue = xArray[x], yValue = yArray[x], touched = False, connectedTo = [])

        
        positions.append(pos)

    print(xArray)
    print(yArray)

def evalDistanceBFS():

    for x in range(len(positions)):
        pos = positions[x]
        connectedTo = pos['connectedTo']

    #find distance between both pos's
    #dist = math.sqrt((xValuep2 - xValuep1)**2 + (yValuep2 - yValuep1)**2)


if __name__ == "__main__":
    setPositions()
    evalDistanceBFS()