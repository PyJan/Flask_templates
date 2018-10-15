#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 21:42:09 2018

@author: jan

file containing HedgeRatio class

"""

import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from bokeh.plotting import figure, output_file, show, reset_output


class HedgeRatio():
    """
    Implementation of hedge ratio model
    
    Usage:
        # create object
        hedgeratio = HedgeRatio()
        
        # simulate spot scenarios
        hedgeratio.runSimulation()
        
        # calculate statistics
        corr = hedgeratio.calculateCorr
        stds = hedgeratio.calculateSTDs
        ratio = hedgeratio.calculateHedgeRatio()
        
        # return scatter plot
        p = hedgeratio.createScatterPlot()
    """
    def __init__(self, rho=0.8, sigmaspot=2, sigmafwd=3, numobserv=1000):
        """
        initialize with default values
        """
        self._rho = rho
        self._sigmaspot = sigmaspot
        self._sigmafwd = sigmafwd
        self._numobserv = numobserv
        self._sim = pd.DataFrame()
        
    def __str__(self):
        return 'Implementation of hedge ratio model'
    
    def __repr__(self):
        return 'HedgeRatio({0}, {1}, {2}, {3})'.format(
                self._rho,
                self._sigmaspot,
                self._sigmafwd,
                self._numobserv)
               
    def runSimulation(self):
        """
        create scenario for daily spot and fwd deltas
        """
        x = DataFrame(np.random.normal(size=(self._numobserv,2)), 
                      columns=['rand1','rand2'])
        self._sim['spot'] = self._sigmaspot*x['rand1']
        self._sim['fwd'] = ((self._rho*x['rand1'] + np.sqrt(1-self._rho**2)*x['rand2'])
                            *self._sigmafwd)
        
    def calculateCorr(self):
        """
        return calculated correlation between spot and fwd
        """
        return round(self._sim.corr().iloc[0,1],3)
    
    def calculateSTDs(self):
        """
        return calculated standard deviations of spot and fwd
        """
        covmatrix = self._sim.cov().applymap(np.math.sqrt)
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
        return self._sim.mul([1,hedgecoef*(-1)]).sum(axis=1).std()
        
    def calculateHedgeStrategies(self, granularity=np.arange(0,2.1,0.05)):
        """
        Simulate hedge strategies for different hedge ratios
        """
        return pd.Series(granularity, index=granularity).map(self.calculateHedgeSTD)
    
    def createScatterPlot(self):
        """
        scatter plot between spot and fwd
        """
        p = figure(title='Spot delta as a function of forward delta', 
                   x_axis_label='Forward delta', y_axis_label='Spot delta')
        p.circle(self._sim['spot'], self._sim['fwd'], size=5)
        return p
        
    def showScatterPlot(self):
        """
        scatter plot visualization
        """
        reset_output()
        output_file('showme2.html')
        show(self.createScatterPlot())
        
    def updateParameters(self, rho=None, sigmaspot=None, sigmafwd=None, numobserv=None):
        """
        update parameters of the model
        """
        if rho is not None:
            self._rho = rho
        if sigmaspot is not None:
            self._sigmaspot = sigmaspot
        if sigmafwd is not None:
            self._sigmafwd = sigmafwd
        if numobserv is not None:
            self._numobserv = numobserv
            
    def getParameters(self):
        """
        return parameters in tuple (rho, sigmaspot, sigmafwd, numobserv)
        """
        return self._rho, self._sigmaspot, self._sigmafwd, self._numobserv
        
if __name__ == '__main__':
    hedgeratio = HedgeRatio()
    hedgeratio.runSimulation()
    #hedgeratio.sim.plot()
    print(hedgeratio.calculateCorr())
    print(hedgeratio.calculateSTDs())
    print(hedgeratio.calculateHedgeRatio())
    print(hedgeratio.calculateHedgeSTD(0.5))
    #hedgeratio.calculateHedgeStrategies().plot()
    hedgeratio.showScatterPlot()
    
        