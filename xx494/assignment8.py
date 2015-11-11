'''
Created on Nov 8, 2015

@author: Xu Xu
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Investment import *


try:
    while True:
    
        positions = raw_input('Please input the list of numbers to check the return : [1, 10, 100, 1000]')
        positions = positions.split(',')
        positions[0] = positions[0][1:]
        positions[-1] = positions[-1][:-1]
        positions = [int(i) for i in positions]
    

        if positions == [1, 10, 100, 1000]:
            num_trails = 10000
            initial_amount = investment(1000)
            results = pd.DataFrame(columns = ["positions", "Mean", "Standard"]) 
        
            n = 0
            for position in positions:
                daily_ret = initial_amount.daily_investment(position, num_trails)
                results.loc[n] = [position, np.mean(daily_ret), np.std(daily_ret)]
                n = n+1
                histogram_plot = plt.figure()
                plt.hist(daily_ret, 100, range = [-1, 1])
                plt.xlabel('Daily Return')
                plt.ylabel('The number of trail with the result')
                plt.title('Position' + str(positions))
            
                histogram_plot.savefig('histogram_{}_pos.pdf'.format(str(position))) 
                results.to_csv('results.txt', sep=',')
            print 'pdf has saved'
        print 'result has been saved'
        
        
   
except KeyboardInterrupt:
        pass
except ValueError:
        pass
    