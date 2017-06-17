import xml.etree.ElementTree
from SourceTrackFactory import *
from SystemTrackFactory import *
from config import *


class XmlReader:
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
            st = stf.createSourceTrack(stEntry.find("trackID"))
            stList.append(st)

        return stList
