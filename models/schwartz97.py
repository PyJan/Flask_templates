#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:25:07 2018

@author: jan

modul with class Schwartz97 for mean-reverting model
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas import DataFrame, Series


class Schwartz97():
    """
    Simulation of Schwartz mean-reverting model.
    """
    
    def __init__(self, alpha=0.05, dt=1, sigma=0.04, mu=3.2, S0=20, steps=100, 
                 numScen=50):
        """
        Input coefficient:\n
        alpha - coefficient of mean reversion\n
        dt - time step\n
        sigma - volatility\n
        mu - long-term level\n
        S0 - initial price\
        steps - number of steps\n
        numScen - number of scenarios
        """
        self._alpha = alpha
        self._dt = dt
        self._sigma = sigma
        self._mu = mu
        self._S0 = S0
        self._steps = steps
        self._numScen = numScen
        self._sim = None
    
    def __str__(self):
        forPrint = """
        Schwartz model with parameters 
        alpha={0} 
        dt={1} 
        sigma={2} 
        mu={3} 
        S0={4}
        step={5}
        numScen={6}
        """
        return forPrint.format(self._alpha, self._dt, self._sigma, self._mu, 
                               self._S0, self._steps, self._numScen)
        
    def __repr__(self):
        return ('Schwartz97(alpha={0}, dt={1}, sigma={2}, mu={3}, S0={4}, ' 
                'steps={5}, numScen={6})'.format(self._alpha, self._dt, 
                self._sigma, self._mu, self._S0, self._steps, self._numScen))
        
    def calculateScenarios(self):
        """
        create scenarios according to formula
        dS = alpha*(mu - ln(S))*S*dt + sigma*S*dz
        """
        S = np.zeros((self._steps, self._numScen))
        dz = (np.random.standard_normal((self._steps, self._numScen))
                                        *np.sqrt(self._dt))
        S[0] = self._S0
        for t in range(1,self._steps):
            S[t]=(S[t-1]+self._alpha*(self._mu-np.log(S[t-1]))*S[t-1]*self._dt
                     +self._sigma*S[t-1]*dz[t-1])
        self._sim = S
        
    def getTimeLabels(self):
        """
        return x axis labels
        """
        return np.array(range(self._steps))*self._dt
    
    def createPyPlot(self):
        """
        create matplotlib.pyplot.plot
        """
        plt.plot(self.getTimeLabels(), self._sim)
        plt.xlabel('Time')
        plt.ylabel('Spot price S')
        return plt
    
        
        
if __name__ == '__main__':
    schwartz97 = Schwartz97()
    print(schwartz97)
    schwartz97.calculateScenarios()
    schwartz97.createPyPlot().show()
    
