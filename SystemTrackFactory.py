from SystemTrack import *

class SystemTrackFactory:
    nextTrackID = 1

    def createSystemTrack(self):
        st = SystemTrack(self.nextTrackID)
        self.nextTrackID += 1

        return st
