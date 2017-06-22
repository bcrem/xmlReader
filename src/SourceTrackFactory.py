from SourceTrack import *

class SourceTrackFactory:
    _nextTrackID = 1


    """
        There's a danger here, that tracks read in will have the same trackID
        as new tracks.  Caller will have to insure this doesn't happen.
    """
    def createSourceTrack(self, trackID):
        if (trackID != None):
            st = SourceTrack(trackID)
        else:
            st = SourceTrack(self._nextTrackID)
            self._nextTrackID += 1

        return st
