# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:43:51 2019

@author: vjha1
"""


import pandas as pd
import numpy as np
import iflvisfirst
import ifrvisfirst


filename = input('Please enter the filename: ' )
df = pd.read_csv (filename)
data1 = df.to_numpy()

LVwhere = np.argwhere(data1 == "Left Ventricle    ")

RVwhere = np.argwhere(data1 == "Right Ventricle     ")

if LVwhere[0,0] > RVwhere [0,0]:
    print('Detected RV Values First')
    print()
    ifrvisfirst.RVfirst2(filename)

elif LVwhere[0,0] < RVwhere [0,0]:
    print('Detected LV Values First')
    print()
    iflvisfirst.LVfirst2(filename)