#!/usr/bin/python

import StatsReader

from Sim import Sim
from config import *


xr = StatsReader.StatsReader(goodFile)
s = Sim()

stList = xr.extractSourceTracks()
s.pushTracks(stList)

systList = xr.extractSystemTracks()
s.pushTracks(systList)

s.listTracks()
