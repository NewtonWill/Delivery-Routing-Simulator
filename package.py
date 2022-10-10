from hashTable import ChainingHashTable


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, destId, specNotes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.destId = destId
        self.specNotes = specNotes

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.deadline,
                                                   self.city, self.zip, self.weight, self.destId, self.specNotes)
    def Get_Package(packageID, HashT):
        return HashT.search(packageID)

    def Get_DestID(packageID, HashT):
        return (HashT.search(packageID)).destId

    # def Get_Distance(originID, destID, dTable):
    #     return dTable[originID, destID]
    #     # dTable is always distanceList in main.py
    #     # destID is found via Get_DestID above using packageID IE Get_DestID(*packageID*)
    #     # originID is from the truck object via get_PositionID(*truckID*)
    #     # transferred to main.py