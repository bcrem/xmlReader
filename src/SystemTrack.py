
class SystemTrack:
    trackID = 0
    contributorList = []  #IDs of contributing sourceTracks

    def __init__(self, tID):
        self.trackID = tID

    def __str__(self):
        return "SystemTrack[" + str(self.trackID) + "]"


    def addContributor(self, id):
        self.contributorList.append(id)
