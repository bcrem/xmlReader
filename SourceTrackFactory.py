from SourceTrack import *

class SourceTrackFactory:
    nextTrackID = 1

    def createSourceTrack(self):
        st = SourceTrack(self.nextTrackID)
        self.nextTrackID += 1

        return st


    def createSourceTrack(self, reader):
        st = SourceTrack(self.nextTrackID)
