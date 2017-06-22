#!/usr/bin/python
import unittest
import sys
sys.path.append("/home/will/work/tracks")
from src.Sim import Sim
from src.SourceTrack import SourceTrack


class SimTestCase(unittest.TestCase):
    def setUp(self):
        self.sim = Sim()

    def tearDown(self):
        self.sim = None


    def test_pushTrack(self):
        self.assertEqual(len(self.sim._sourceTracks), 0)
        self.sim.pushTrack(SourceTrack(1))
        self.assertEqual(len(self.sim._sourceTracks), 1)
        self.assertEqual(self.sim._sourceTracks[0].trackID, 1)


    def test_pushTracks(self):
        self.assertEqual(len(self.sim._sourceTracks), 0)
        l = [SourceTrack(1), SourceTrack(2), SourceTrack(3),]
        self.sim.pushTracks(l)
        self.assertEqual(len(self.sim._sourceTracks), 3)
        self.assertEqual(self.sim._sourceTracks[0].trackID, 1)
        self.assertEqual(self.sim._sourceTracks[1].trackID, 2)
        self.assertEqual(self.sim._sourceTracks[2].trackID, 3)


if __name__ == '__main__':
    unittest.main()
