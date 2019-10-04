# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:18:02 2019

@author: vjha1
"""

import pandas as pd
import numpy as np
#import csv

df = pd.read_csv (r'filename.csv')
data1 = df.to_numpy()

patientwhere = np.argwhere(data1 == "Patient")
pnamefull = data1[patientwhere[0,0]]
pnamefull = pnamefull.tolist()
pnamefull.pop(0)
fullname = pnamefull[0]

Name = fullname.split(',')


