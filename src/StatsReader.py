import xml.etree.ElementTree
from SourceTrackFactory import *
from SystemTrackFactory import *
from config import *


class StatsReader:
    root = None

    def __init__(self, filename):
        self.root = xml.etree.ElementTree.parse(filename).getroot()


    """
        Returns a list of sourceTracks extracted from the
        xml file.
    """
    def extractSourceTracks(self):
        stList = []
        stf = SourceTrackFactory()

        stEntries = self.root.findall("sourceTrack")

        for stEntry in stEntries:
            idElem = stEntry.find("trackID")
            st = stf.createSourceTrack(idElem.text)
            stList.append(st)

        return stList


    """
        Returns a list of systemTracks extracted from the
        xml file.
    """
    def extractSystemTracks(self):
        systList = []
        systf = SystemTrackFactory()

        systEntries = self.root.findall("systemTrack")

        for systEntry in systEntries:
            idElem = systEntry.find("trackID")
            syst = systf.createSystemTrack(idElem.text)
            #TODO: fill contributorList
            systList.append(syst)

        return systList
