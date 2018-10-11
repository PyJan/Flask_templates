#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:42:09 2018

@author: jan
"""
import pandas as pd
import numpy as np
from pandas import DataFrame, Series


class HedgeRatio():
    """
    object for simulation and presentation
    of hedge ratio for cross-hedge
    """
    def __init__(self):
        """
        initialize with default values
        """
        self.rho = 0.81
        self.sigmaspot = 2
        self.sigmafwd = 3
        self.numobserv = 1000
        self.sim = pd.DataFrame()
    def runSimulation(self):
        """
        create spot scenario
        """
        x = DataFrame(np.random.normal(size=(self.numobserv,2)), 
                      columns=['rand1','rand2'])
        self.sim['spot'] = self.sigmaspot*x['rand1']
        self.sim['fwd'] = ((self.rho*x['rand1'] + np.sqrt(1-self.rho**2)*x['rand2'])
                            *self.sigmafwd)
        
if __name__ == '__main__':
    hedgeratio = HedgeRatio()
    hedgeratio.runSimulation()
    hedgeratio.sim.plot()
    print(hedgeratio.sim.corr())
    print(hedgeratio.sim.cov())
        
        