import xml.etree.ElementTree
from config import *


class XmlReader:

    def __init__(self, filename):
        root = xml.etree.ElementTree.parse(filename).getroot()

        for key in tdmKeys:
            k = root.find(key)
            print(k)
