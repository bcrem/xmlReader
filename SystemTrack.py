
class SystemTrack:
    trackID = 0

    def __init__(self, tID):
        self.trackID = tID

    def __str__(self):
        return "SystemTrack[" + str(self.trackID) + "]"
