#!/usr/bin/python

from Sim import Sim
from config import *


import XmlReader


xr = XmlReader.XmlReader(goodFile)
s = Sim()

stList = xr.extractSourceTracks()
s.pushSourceTracks(stList)

s.listSourceTracks()
