
class SourceTrack:
    trackID = 0
    timeIntroduced = None
    timeTracked = None


    def __init__(self, tID):
        self.trackID = tID

    def __str__(self):
        return "SourceTrack[" + str(self.trackID) + "]"
