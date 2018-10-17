#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:00:40 2018

@author: jan

unit test for hedgeratio model
"""

import unittest
from ..hedgeratio import HedgeRatio

class HedgeRatioTestCase(unittest.TestCase):
    """
    class for HedgeRatio unit test
    """
    def test_simulation(self):
        """
        test if simulation was run properly
        """
        hedgeratio = HedgeRatio()
        hedgeratio.runSimulation()
        self.assertEqual(hedgeratio._sim.size, 2*hedgeratio._numobserv, 
                         'Simulation not properly generated - wrong size.')
        
def runTest():
    unittest.main()