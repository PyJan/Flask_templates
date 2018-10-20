#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:25:07 2018

@author: jan

modul with class Schwartz97 for mean-reverting model
"""

class Schwartz97():
    """
    Simulation of Schwartz mean-reverting model.
    """
    
    def __init__(self, alpha=0.05, dt=1, sigma=0.04, mu=3.2, S0=20):
        """
        Input coefficient:\n
        alpha - coefficient of mean reversion\n
        dt - time step\n
        sigma - volatility\n
        mu - long-term level\n
        S0 - initial price
        """
        self._alpha = alpha
        self._dt = dt
        self._sigma = sigma
        self._mu = mu
        self._S0 = S0
    
    def __str__(self):
        forPrint = """
        Schwartz model with parameters 
        alpha={0} 
        dt={1} 
        sigma={2} 
        mu={3} 
        S0={4}
        """
        return forPrint.format(self._alpha, self._dt, 
                               self._sigma, self._mu, self._S0)
        
    def __repr__(self):
        return 'Schwartz97(alpha={0}, dt={1}, sigma={2}, mu={3}, S0={4})'.format(
                self._alpha, self._dt, self._sigma, self._mu, self._S0)
        
    
        
        
if __name__ == '__main__':
    schwartz97 = Schwartz97()
    print(schwartz97)
    