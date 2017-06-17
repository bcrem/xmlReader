#!/usr/bin/python

from Sim import Sim
from SourceTrackFactory import *
from SystemTrackFactory import *


s = Sim()
stf = SourceTrackFactory()
systf = SystemTrackFactory()

s.pushSourceTrack(stf.createSourceTrack())
s.pushSourceTrack(stf.createSourceTrack())
s.pushSourceTrack(stf.createSourceTrack())
s.pushSourceTrack(stf.createSourceTrack())

st = s.popSourceTrack()
print st

s.listSourceTracks()
