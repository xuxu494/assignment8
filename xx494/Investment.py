'''
Created on Nov 8, 2015

@author: Xu Xu
'''
import numpy as np

class investment():
    def __init__(self, investment_value):
        if investment_value > 0:
            self.investment_value = investment_value
        else:
            raise ValueError
            print "Positions need to be positive"
        
    def daily_investment(self, position, num_trails):
        position_value = self.investment_value/position
        cumu_ret = []
        daily_ret = []
        for i in range(10000):
            cumu_ret.append((np.random.choice([2, 0], size = position, p=[0.51, 0.49]).sum())*position_value)
        for ret in cumu_ret:
            daily_ret.append((ret/float(self.investment_value))-1)
        return daily_ret
