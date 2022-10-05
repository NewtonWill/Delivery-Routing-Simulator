import csv

# script on this page loads distanceTable.csv into reader, fills in blank data, and returns full list


def loadDistanceData():
    with open('distanceTable.csv') as distanceTable:
        reader = csv.reader(distanceTable, delimiter=',')
        distanceList = list(reader)
        for x in range(27):
            for y in range(27):
                if len(distanceList[x][y]) == 0:
                    distanceList[x][y] = distanceList[y][x]
        return distanceList

