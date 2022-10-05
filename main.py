#import Truck
from Truck import Truck
import distance
#import package
from package import Package
import hashTable
import csv

packageTable = hashTable.ChainingHashTable(40)


def loadPackageData():
    with open('packages.csv') as packageList:
        packageData = csv.reader(packageList, delimiter=',')
        next(packageData)  # skip header
        for pkg in packageData:
            pID = int(pkg[0])
            pAddress = pkg[1]
            pCity = pkg[2]
            pState = pkg[3]
            pZip = pkg[4]
            pDeadline = pkg[5]
            pWeight = pkg[6]
            pDestId = pkg[7]
            pSpecNotes = pkg[8]

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip,
                                pDeadline, pWeight, pDestId, pSpecNotes)
            #print(p)

            # insert it into the hash table
            packageTable.insert(pID, p)

def deliveryalgo(truck, packagelist, dList):
    minDist = 0
    for truck.packagesLoaded in packagelist:
        print(truck.packagesLoaded.id)
        i = truck.packagesLoaded.id
        #print(Package.Get_Distance(truck.get_PositionID(), Package.Get_DestID(i, packageTable), dList))



loadPackageData() #Do Above

distanceList = distance.loadDistanceData()

truck1 = Truck(1, [packageTable.search(1),
                         packageTable.search(3),
                         packageTable.search(5),
                         packageTable.search(7),
                         packageTable.search(8),
                         packageTable.search(9),
                         packageTable.search(10),
                         packageTable.search(13),
                         packageTable.search(14),
                         packageTable.search(15),
                         packageTable.search(16),
                         packageTable.search(19),
                         packageTable.search(20),
                         packageTable.search(21),
                         packageTable.search(27),
                         packageTable.search(29),
                         packageTable.search(30),
                         packageTable.search(34),
                         packageTable.search(35),
                         packageTable.search(37),
                         packageTable.search(38),
                         packageTable.search(39),
                         ],
                     0)

truck2 = Truck(2, [packageTable.search(11),
                         packageTable.search(18),
                         packageTable.search(22),
                         packageTable.search(23),
                         packageTable.search(24),
                         ],
                     0)

truck3 = Truck(3, [
                         packageTable.search(2),
                         packageTable.search(4),
                         packageTable.search(6),
                         packageTable.search(12),
                         packageTable.search(17),
                         packageTable.search(25),
                         packageTable.search(26),
                         packageTable.search(28),
                         packageTable.search(31),
                         packageTable.search(32),
                         packageTable.search(33),
                         packageTable.search(36),
                         packageTable.search(40)
                         ],
                     0)

print(packageTable.search(1))

print(truck1)
print(truck2)
print(truck3)

print("Total truck mileage: %s" %
      (truck1.currentMileage + truck2.currentMileage + truck3.currentMileage))

deliveryalgo(truck2, truck2.packagesLoaded, distanceList)

#print(truck2.packagesLoaded)

print(Package.Get_Package(hashTable., packageTable))