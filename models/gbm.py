#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 19:28:54 2018

@author: jan

contains class for simulation of Geometric Brownian Motion
"""

import pandas as pd
import numpy as np

from pandas import DataFrame
from bokeh.plotting import show, figure
from bokeh.io import reset_output
from bokeh.palettes import Paired12




class GBM():
    """
    container for Geometric Brownian Motion simulation
    
    formula: dS / S = mu * dt + sigma * dZ         
    """
    
    def __init__(self, mu=0.05, sigma=0.01, S0=50, dt=0.02, steps=50, numScen=10):
        """
        parameters:
            
            mu: drift \n
            sigma: volatility \n
            S0: initial spot price \n
            dt: time step \n
            steps: number of steps \n
            numScen: number of scenarios \n
        """        
        self._mu = mu
        self._sigma = sigma
        self._S0 = S0
        self._dt = dt
        self._steps = steps
        self._numScen = numScen
        self._sim = None
        
    def calculateScenarios(self):
        """
        sceate scenarios and fill self._sim with them
        """
        self._sim = np.zeros((self._steps, self._numScen))
        self._sim[0] = self._S0
        for i in range(self._steps-1):
            dZ = np.random.normal(scale=np.sqrt(self._dt), size=self._numScen)
            self._sim[i+1] = ((self._mu * self._dt + self._sigma * dZ) 
                               * self._sim[i] + self._sim[i])
        columns = ['S{:03d}'.format(i+1) for i in range(self._numScen)]
        self._sim = DataFrame(self._sim, columns=columns, 
                              index=np.arange(self._steps)*self._dt)
    
    def createPlot(self):
        """
        create Bokeh plot of scenarios
        """
        p = figure(width=400, height=400)
        p.multi_line(xs=[self._sim.index]*self._numScen,
                     ys=[self._sim[col].values for col in self._sim],
                     line_width=2, 
                     line_color=(Paired12*(self._numScen//12+1))[:self._numScen])
        return p
        
        
if __name__ == '__main__':
    gbm = GBM()
    gbm.calculateScenarios()
    reset_output()
    p = gbm.createPlot()
    show(p)