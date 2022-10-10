from hashTable import ChainingHashTable


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, destId, specNotes, deliveryStatus):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.destId = destId
        self.specNotes = specNotes
        self.deliveryStatus = deliveryStatus

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.deadline,
                                                   self.city, self.zip, self.weight, self.destId,
                                                   self.specNotes, self.deliveryStatus)
    def Get_Package(packageID, HashT):
        return HashT.search(packageID)

    def Get_DestID(packageID, HashT):
        return (HashT.search(packageID)).destId