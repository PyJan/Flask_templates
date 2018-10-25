#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 19:28:54 2018

@author: jan
"""

"""
contains class for simulation of Geometric Brownian Motion
"""

class GBM():
    """
    container for Geometric Brownian Motion simulation
    
    formula: dS / S = mu * dt + sigma * dZ         
    """
    
    def __init__(self, mu=0.05, sigma=0.01, S0=50, dt=1, steps=50, numScen=10):
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
        
        
if __name__ = '__main__':
    gbm = GBM()