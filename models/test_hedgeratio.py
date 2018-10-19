#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:00:40 2018

@author: jan

unit test for hedgeratio model
"""

import unittest
from hedgeratio import HedgeRatio
from bokeh.plotting.figure import Figure

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
        
    def test_corr(self):
        """
        test that correlation is in <-1,1>
        """
        hedgeratio = HedgeRatio()
        hedgeratio.runSimulation()        
        self.assertLessEqual(hedgeratio.calculateCorr()**2, 1, 
                             'Impossible value for correlation')
        
    def test_scatterplot(self):
        """
        test existence of scatter plot
        """
        hedgeratio = HedgeRatio()
        hedgeratio.runSimulation()
        self.assertIsInstance(hedgeratio.createScatterPlot(), Figure)         
        
        
unittest.main()