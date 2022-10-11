from Truck import Truck
import distance
from package import Package
import hashTable
import csv
import datetime

packageTable = hashTable.ChainingHashTable(40)


def Get_Distance(originID, destID, dTable):
    return dTable[originID][destID]
    # dTable is always distanceList in main.py
    # destID is found via Get_DestID above using packageID IE Get_DestID(*packageID*)
    # originID is from the truck object via get_PositionID(*truckID*)

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

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
                                pDeadline, pWeight, pDestId, pSpecNotes, "At the Hub")
            #print(p)

            # insert it into the hash table
            packageTable.insert(pID, p)

def calculateTime(miles):
    return round(miles/18, 3)

def printDeadlines():
    for i in range(41):
        if i > 0:
            if Package.Get_Package(i, packageTable).deadline == "EOD":
                print("Package ID: " + str(i) + "\t\tDeadline: " + str(
                    Package.Get_Package(i, packageTable).deadline) + "\t\t\t" + str(
                    Package.Get_Package(i, packageTable).deliveryStatus))
            else:
                print("Package ID: " + str(i) + "\t\tDeadline: " + str(
                    Package.Get_Package(i, packageTable).deadline) + "\t\t" + str(
                    Package.Get_Package(i, packageTable).deliveryStatus))


def deliveryalgo(truck, packagelist, dList):
    deliveredPackages = []
    print("Truck " + str(truck.id) + " Starting Time: " + str(truck.currentTime))
    while len(packagelist) > 0:
        minDist = float(100)
        closest = None
        for truck.packagesLoaded in packagelist:
            prCyan("--------------------------------------------------------------------------")
            print("Package:", truck.packagesLoaded.id)
            i = truck.packagesLoaded.id
            print("Current Truck Position:", truck.get_PositionID())
            print("Package Destination:", Package.Get_DestID(i, packageTable))
            currentDist = float(Get_Distance(int(truck.get_PositionID()), int(Package.Get_DestID(i, packageTable)), dList))
            print("CurrentDist:", currentDist)
            if currentDist < minDist:
                minDist = currentDist
                closest = i
            print("Closest: Package", closest, "|| Distance: ", minDist)
        truck.currentPosition = Package.Get_DestID(closest, packageTable)
        truck.currentMileage = round(truck.currentMileage + minDist, 1)
        truck.currentTime = truck.currentTime + datetime.timedelta(hours=calculateTime(minDist))
        deliveredPackages.append(closest)
        prYellow("//////////////////////////////////////////////////////////////////////////")
        print("Delivering package (", closest, ")\nCurrent truck mileage: ", truck.currentMileage)
        print("Current time: ", truck.currentTime)
        print("Delivered Packages: ", deliveredPackages)
        prYellow("//////////////////////////////////////////////////////////////////////////")
        prRed("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        Package.Get_Package(closest, packageTable).deliveryStatus = "Delivered at " + str(truck.currentTime)
        packagelist.remove(Package.Get_Package(closest, packageTable))
    if truck.id == 3:
        #return to hub to launch truck 2
        returnDist = float(Get_Distance(int(truck.currentPosition), 0, distanceList))
        truck.currentTime = truck.currentTime + datetime.timedelta(hours=calculateTime(returnDist))
        truck.currentMileage = round(truck.currentMileage + returnDist, 1)
        truck.currentPosition = 0


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

deliveryalgo(truck1, truck1.packagesLoaded, distanceList)

deliveryalgo(truck3, truck3.packagesLoaded, distanceList)

truck2.currentTime = truck3.currentTime  # driver returns to hub and switches to truck 2
deliveryalgo(truck2, truck2.packagesLoaded, distanceList)


print("\nTruck 1 Miles: ", truck1.currentMileage, "\nTruck 1 Hours: ", calculateTime(truck1.currentMileage))
print("Final Delivery: ", truck1.currentTime)
print("\nTruck 2 Miles: ", truck2.currentMileage, "\nTruck 2 Hours: ", calculateTime(truck2.currentMileage))
print("Final Delivery: ", truck2.currentTime)
print("\nTruck 3 Miles: ", truck3.currentMileage, "\nTruck 3 Hours: ", calculateTime(truck3.currentMileage))
print("Final Delivery: ", truck3.currentTime)
print("\nTotal truck miles: ", round(truck1.currentMileage + truck2.currentMileage + truck3.currentMileage, 2), "\n")

printDeadlines()
