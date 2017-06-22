from SystemTrack import *

class SystemTrackFactory:
    _nextTrackID = 1

    def createSystemTrack(self, trackID):
        if (trackID != None):
            st = SystemTrack(trackID)
        else:
            st = SystemTrack(self._nextTrackID)
            self._nextTrackID += 1

        return st
