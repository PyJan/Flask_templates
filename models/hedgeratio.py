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
        create scenario for daily spot and fwd deltas
        """
        x = DataFrame(np.random.normal(size=(self.numobserv,2)), 
                      columns=['rand1','rand2'])
        self.sim['spot'] = self.sigmaspot*x['rand1']
        self.sim['fwd'] = ((self.rho*x['rand1'] + np.sqrt(1-self.rho**2)*x['rand2'])
                            *self.sigmafwd)
        
    def calculateCorr(self):
        """
        return calculated correlation between spot and fwd
        """
        return round(hedgeratio.sim.corr().iloc[0,1],3)
    
    def calculateSTDs(self):
        """
        return calculated standard deviations of spot and fwd
        """
        covmatrix = hedgeratio.sim.cov().applymap(np.math.sqrt)
        return round(covmatrix.iloc[0,0], 3), round(covmatrix.iloc[1,1], 3)
    
    def calculateHedgeRatio(self):
        """
        return calculated hedge ratio from stats
        """
        return round(self.calculateCorr()*
                     self.calculateSTDs()[0]
                     /self.calculateSTDs()[1],3)
        
    def calculateHedgeSTD(self, hedgecoef):
        """
        standard deviation of 1 hedge strategy
        """
        return self.sim.mul([1,hedgecoef*(-1)]).sum(axis=1).std()
        
    def calculateHedgeStrategies(self, granularity=np.arange(0,2.1,0.05)):
        """
        Simulate hedge strategies for different hedge ratios
        """
        return pd.Series(granularity, index=granularity).map(self.calculateHedgeSTD)
        
        
if __name__ == '__main__':
    hedgeratio = HedgeRatio()
    hedgeratio.runSimulation()
    hedgeratio.sim.plot()
    print(hedgeratio.calculateCorr())
    print(hedgeratio.calculateSTDs())
    print(hedgeratio.calculateHedgeRatio())
    print(hedgeratio.calculateHedgeSTD(0.5))
    hedgeratio.calculateHedgeStrategies().plot()
    
        