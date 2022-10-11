import datetime

class Truck:
    def __init__(self, id, packagesLoaded, currentPosition):
        self.id = id
        self.packagesLoaded = packagesLoaded
        self.currentPosition = currentPosition
        self.currentMileage = 0
        self.currentTime = datetime.timedelta(hours=8)

    def __str__(self):
        return "Truck #%s // Packages: %s // Current Position ID: %s // Current Mileage: %s" % \
               (self.id, self.printpackageload(self.packagesLoaded),
                self.currentPosition, self.currentMileage)

    def printpackageload(self, packageLoad):
        TPackageList = []
        for i in packageLoad:
            TPackageList.append(str(i.id))

        return ", ".join(TPackageList)

    def get_PositionID(self):
        return self.currentPosition
