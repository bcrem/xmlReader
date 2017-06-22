class Sim:

    def __init__(self):
        self._sourceTracks = []
        self._systemTracks = []


    def listTracks(self):
        for st in self._sourceTracks:
            print st

        for syst in self._systemTracks:
            print syst


    def pushTrack(self, trk):
        if (trk != None):
            if trk.__class__.__name__ == "SystemTrack":
                self._systemTracks.append(trk)
            else:
                self._sourceTracks.append(trk)

    def pushTracks(self, trkList):
        if (len(trkList) > 0):
            if trkList[0].__class__.__name__ == "SystemTrack":
                self._systemTracks.extend(trkList)
            else:
                self._sourceTracks.extend(trkList)
