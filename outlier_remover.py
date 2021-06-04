# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:38:28 2021

The following program recursively removes outliers of a dataset
"""


import numpy as np

# seed the random number generator
np.random.seed(1)

# generate univariate observations
sample = list(7 * np.random.randn(100) + 6)

#sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 1000, 10000]
cutoff = 3

def clean_mean_auto(sample, cutoff):
    new = []
    old = sample
    while old != new:
        old = sample                                 # "sample" is recyled as a parameter in the loop
        data_mean = np.mean(old) 
        data_std = np.std(old)
        cut_off_val = data_std * cutoff
        lower = data_mean - cut_off_val
        upper = data_mean + cut_off_val
        new = [x for x in old if x >= lower and x <= upper]  
        sample = new
        #print(old)
        #print(new)
        #print('\n')
    print(new)
    return round(np.mean(new),2)

print('The mean without outliers is: %f' % clean_mean_auto(sample, cutoff))