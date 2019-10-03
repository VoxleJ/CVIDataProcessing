# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:34:59 2019

@author: vjha1
"""

import pandas as pd
import numpy as np

#np.set_printoptions(threshold=np.inf)
#np.set_printoptions(edgeitems=3,infstr='inf', linewidth=75, nanstr='nan', precision=8, suppress=False, threshold=1000, formatter=None)

df = pd.read_csv (r'filename.csv')

data1 = df.to_numpy()

#print(np.argwhere(data1 == "Shah,Sharista"))

torsionwhere = np.argwhere(data1 == "torsion")


RVTorsion = data1[torsionwhere[0,0]]
RVTorsion = RVTorsion.tolist()
RVTorsion.pop(0)
del RVTorsion[20:26]
RVTorsion = max(RVTorsion)

print(RVTorsion)



LVTorsion = data1[torsionwhere[1,0]]
LVTorsion = LVTorsion.tolist()
LVTorsion.pop(0)
print(LVTorsion)
del LVTorsion[20:26]
LVTorsion = max(LVTorsion)

print(LVTorsion)
