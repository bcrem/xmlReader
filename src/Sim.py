class Sim:
    sourceTracks = []
    systemTracks = []

    def listTracks(self):
        for st in self.sourceTracks:
            print st

        for syst in self.systemTracks:
            print syst

    def pushTrack(self, trk):
        if (trk != None):
            if trk.__class__.__name__ == "SystemTrack":
                self.systemTracks.append(trk)
            else:
                self.sourceTracks.append(trk)

    def pushTracks(self, trkList):
        if (len(trkList) > 0):
            if trkList[0].__class__.__name__ == "SystemTrack":
                self.systemTracks.extend(trkList)
            else:
                self.sourceTracks.extend(trkList)
