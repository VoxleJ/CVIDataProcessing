# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:53:05 2019

@author: vjha1
"""

import pandas as pd
import numpy as np

#np.set_printoptions(threshold=np.inf)
np.set_printoptions(edgeitems=3,infstr='inf', linewidth=75, nanstr='nan', precision=8, suppress=False, threshold=1000, formatter=None)

df = pd.read_csv (r'Shah_Sharista_2002-04-25_Scientific_Report_2019-10-03.csv')


data1 = df.to_numpy()

print(np.argwhere(data1 == "Shah,Sharista"))

Globewhere = np.argwhere(data1 == "Global")

for i in range(len(Globewhere)):
   print(data1[Globewhere[i,0]])

abc = data1[32]
a = Globewhere[1]

abcd = abc.tolist()

RVSax = data1[Globewhere[0,0]]
print(RVSax)


#print(data1[74,1])

#print(data1[32,:])