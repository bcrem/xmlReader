class Sim:
    sourceTracks = []

    def listSourceTracks(self):
        for st in self.sourceTracks:
            print st

    def pushSourceTrack(self, st):
        self.sourceTracks.append(st)

    def pushSourceTracks(self, stList):
        self.sourceTracks.extend(stList)

    def popSourceTrack(self):
        st = self.sourceTracks.pop()

        return st
