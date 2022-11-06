#William Newton 001451491
from Truck import Truck
import distance
from package import Package
import hashTable
import csv
import datetime
import time

packageTable = hashTable.ChainingHashTable(40)
#hash table created


def checkForDdl():
    #Function used to check for package deadline and print if it has been met
    for i in range(41):
        if i > 0:
            print("Package: ", str(Package.Get_Package(i, packageTable).id))
            if Package.Get_Package(i, packageTable).deadline == "EOD":
                print("Deadline: EOD, No delivery constraint")
                print("Delivery Time:", parseStatus(i))
                prGreen("Package Deadline Met (No Deadline Constraint)")  # Ignore packages with no deadline
            else:
                dline = parseDeadline(i)
                print("Deadline:", dline)
                stat = Package.Get_Package(i, packageTable).deliveryStatus
                status = stat.split(' ')
                deliverytime = status[2].split(":")
                truedeliverytime = datetime.timedelta(hours= int(deliverytime[0]), minutes= int(deliverytime[1]))
                print("Delivery Time:", truedeliverytime)
                if truedeliverytime > dline:
                    prRed("Delivery Deadline Error: Delivery time is past deadline")
                else:
                    prGreen("Package Deadline Met")


def parseDeadline(PID):
    #Function used to parse package deadline and output in time format
    this = Package.Get_Package(PID, packageTable).deadline
    words = this.split(':')
    words2 = words[1].split(' ')
    dline = datetime.timedelta(hours=AMPM(words2[1], int(words[0])), minutes=int(words2[0]))
    return dline


def parseStatus(PID):
    #Function used to parse package status for delivery time
    stat = Package.Get_Package(PID, packageTable).deliveryStatus
    status = stat.split(' ')
    deliverytime = status[2].split(":")
    truedeliverytime = datetime.timedelta(hours=int(deliverytime[0]), minutes=int(deliverytime[1]))
    return truedeliverytime


def AMPM(ampm, hour):
    #Function used in conjunction with parseDeadline to determine 24 hour standard
    if ampm == 'AM':
        return hour
    if ampm == 'PM':
        return hour+12


def Get_Distance(originID, destID, dTable):
    #Function used to locate distance values using 2 location IDs
    return dTable[originID][destID]
    # dTable is always distanceList in main.py
    # destID is found via Get_DestID above using packageID IE Get_DestID(*packageID*)
    # originID is from the truck object via get_PositionID(*truckID*)


# all below are used to support readability of user interface data
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


def loadPackageData():
    #Function used to load packages from csv into memory
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
    #used to calculate passage of time via miles per hour
    return round(miles/18, 3)


def printDeadlines():
    #used to display all packages, their deadlines, and their delivery time
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
    #Main algorithm used to determine delivery route and assign data
    prPurple("Truck: " + str(truck.id))
    prPurple("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    deliveredPackages = [] # used to print list for user
    corrected = False # Flag used for special package 9 case
    truck.startingTime = truck.currentTime
    print("Truck " + str(truck.id) + " Starting Time: " + str(truck.startingTime))
    while len(packagelist) > 0:
        minDist = float(100) # assigned as higher number than intended delivery
        closest = None # determines the closest package id
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
                closest = i # assigns new closest distance if conditions are met
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
        prRed("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        Package.Get_Package(closest, packageTable).deliveryStatus = "Delivered at " + str(truck.currentTime)
        packagelist.remove(Package.Get_Package(closest, packageTable))
        if corrected is False and (truck.currentTime > datetime.timedelta(hours=10, minutes=20)):
            corrected = True
            Package.Get_Package(9, packageTable).specNotes = "Package address and destination ID has been " \
                                                             "modified as of 10:20 AM. All post-delivery " \
                                                             "inquiries will reflect corrected information"
            Package.Get_Package(9, packageTable).destId = 19
            Package.Get_Package(9, packageTable).address = "410 S State St."
            Package.Get_Package(9, packageTable).zip = 84111
    if truck.id == 3:
        #return to hub to launch truck 2
        returnDist = float(Get_Distance(int(truck.currentPosition), 0, distanceList))
        truck.currentTime = truck.currentTime + datetime.timedelta(hours=calculateTime(returnDist))
        truck.currentMileage = round(truck.currentMileage + returnDist, 1)
        truck.currentPosition = 0


loadPackageData()
#package data is loaded from csv

distanceList = distance.loadDistanceData()
#distance data is loaded from csv

truck1 = Truck(1, [
                        packageTable.search(1),
                        packageTable.search(5),
                        packageTable.search(7),
                        packageTable.search(8),
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
                        packageTable.search(39),
                        ], 0)

truck2 = Truck(2, [
                        packageTable.search(3),
                        packageTable.search(6),
                        packageTable.search(9),
                        packageTable.search(11),
                        packageTable.search(18),
                        packageTable.search(22),
                        packageTable.search(23),
                        packageTable.search(24),
                        packageTable.search(25),
                        packageTable.search(28),
                        packageTable.search(32),
                        packageTable.search(36),
                        packageTable.search(38),
                        ], 0)

truck3 = Truck(3, [
                        packageTable.search(2),
                        packageTable.search(4),
                        packageTable.search(12),
                        packageTable.search(17),
                        packageTable.search(26),
                        packageTable.search(31),
                        packageTable.search(33),
                        packageTable.search(40)
                        ], 0)
#All trucks are manually initiated and loaded with packages from package hash table

truck1.packageHistory = Truck.pckghistory(truck1, truck1.packagesLoaded)
truck2.packageHistory = Truck.pckghistory(truck2, truck2.packagesLoaded)
truck3.packageHistory = Truck.pckghistory(truck3, truck3.packagesLoaded)
#List of packages that were loaded onto truck is saved for data auditing purposes

deliveryalgo(truck1, truck1.packagesLoaded, distanceList)

deliveryalgo(truck3, truck3.packagesLoaded, distanceList)

truck2.currentTime = truck3.currentTime  # driver returns to hub and switches to truck 2
deliveryalgo(truck2, truck2.packagesLoaded, distanceList)
#All trucks are sent to deliver packages


def TFinalStats():
    #Function is used to display statistics for truck miles and hours
    print("\nTruck 1 Miles: ", truck1.currentMileage, "\nTruck 1 Hours: ", calculateTime(truck1.currentMileage))
    print("Final Delivery: ", truck1.currentTime)
    print("\nTruck 2 Miles: ", truck2.currentMileage, "\nTruck 2 Hours: ", calculateTime(truck2.currentMileage))
    print("Final Delivery: ", truck2.currentTime)
    print("\nTruck 3 Miles: ", truck3.currentMileage, "\nTruck 3 Hours: ", calculateTime(truck3.currentMileage))
    print("Final Delivery: ", truck3.currentTime)
    print("\nTotal truck miles: ", round(truck1.currentMileage + truck2.currentMileage + truck3.currentMileage, 2), "\n")


prLightPurple('-------------------------------------------------------------------------')
printDeadlines()
#Displays when a package should have been delivered
prLightPurple('-------------------------------------------------------------------------')
checkForDdl()
#Displays if the deadline has been met for each package


def timeAudit(PID, TInput):
    #Function returns what the status of a package should be at a specified time
    Ptime = parseStatus(PID)
    if TInput <= datetime.timedelta(hours=8):
        return "Time: " + str(TInput) + " // Truck #" + str(whichTruck(PID)) + " // Package " + str(PID) + " At the Hub"
    if Ptime <= TInput:
        return "Time: " + str(TInput) + " // Truck #" + str(whichTruck(PID)) + " // Package " + str(PID) + ' ' + str(packageTable.search(PID).deliveryStatus)
    if PID in truck1.packageHistory or PID in truck3.packageHistory:
        return "Time: " + str(TInput) + " // Truck #" + str(whichTruck(PID)) + " // Package " + str(PID) + " En Route; To be " + str(packageTable.search(PID).deliveryStatus)
    if whichTruck(PID) == 2:
        if TInput <= truck2.startingTime:
            return "Time: " + str(TInput) + " // Truck #" + str(whichTruck(PID)) + " // Package " + str(PID) + " At the Hub"
        else:
            return "Time: " + str(TInput) + " // Truck #" + str(whichTruck(PID)) + " // Package " + str(PID) + " En Route; To be " + str(
                packageTable.search(PID).deliveryStatus)
    else:
        return "package not found in truck history"


def showAllByTime():
    #Function utilizes timeAudit to display all package statuses at a specified time
    x = int(input("Please specify hour(24hr format): "))
    y = int(input("Please specify minute: "))
    z = datetime.timedelta(hours=x, minutes=y)
    for i in range(41):
        if i > 0:
            print(timeAudit(i, z))


def whichTruck(PID):
    #Function used to determine which truck a package was loaded onto
    if PID in truck1.packageHistory:
        return 1
    if PID in truck2.packageHistory:
        return 2
    if PID in truck3.packageHistory:
        return 3


def Audit():
    #Function used by the end user to verify data on a specific package, all packages, or trucks
    print("\nPress 1 to search by package number\nPress 2 to search all by time\n"
          "Press 3 to show truck mileage\nPress 4 to Exit")
    ans = input()
    realanswer = False
    if ans == str("1"):
        realanswer = True
        PID = int(input("Please enter Package ID: "))
        print(packageTable.search(PID), '\n\nSearch for status at a specific time? (Y/N)')
        if YesNo(input()):
            hrs = int(input("Please specify hour(24hr format): "))
            mins = int(input("Please specify minute: "))
            print(timeAudit(PID, datetime.timedelta(hours=hrs, minutes=mins)))
            Audit()
        else:
            print("Returning to main menu")
            Audit()

    if ans == str("2"):
        realanswer = True
        showAllByTime()
        Audit()
    if ans == str("3"):
        realanswer = True
        TFinalStats()
        Audit()
    if ans == str("4"):
        realanswer = True
        print('Exiting Program...')
    if realanswer is False:
        print('Answer Undefined')
        Audit()


def YesNo(answer):
    #Function used during Audit to parse for an affirmative answer
    if (answer == "Y") or (answer == "y") or (answer == "Yes") or (answer == "yes"):
        return True
    else:
        return False


Audit()
#All deliveries have been made and function for data retrieval is called and then
# controlled by the user
