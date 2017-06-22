#!/usr/bin/python

import StatsReader

from Sim import Sim
from config import *


def processEventLog(log):
    """
    Given an event.log file produced by the Monitor, processEventLog()
    will read in the events line-by-line and
    """
    pass


xr = StatsReader.StatsReader(goodFile)
s = Sim()

stList = xr.extractSourceTracks()
s.pushTracks(stList)

systList = xr.extractSystemTracks()
s.pushTracks(systList)

s.listTracks()
