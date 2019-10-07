# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:53:27 2019

@author: vjha1
"""
import pandas as pd
import numpy as np
import csv


df = pd.read_csv (r'Shah_Sharista_2002-04-25_Scientific_Report_2019-10-04.csv')
data1 = df.to_numpy()

#LV Measurements

#Global Results Table RV2D, LV2D, LV3D
Globewhere = np.argwhere(data1 == "Global")

RVSax = data1[Globewhere[0,0]]
RVSax = RVSax.tolist()
del RVSax[0:2]
#print(RVSax)

RVLax = data1[Globewhere[1,0]]
RVLax = RVLax.tolist()
del RVLax[0:2]
#print(RVLax)

#skip data1[Globewhere[2,0]]

LVSax = data1[Globewhere[3,0]]
LVSax = LVSax.tolist()
del LVSax[0:2]
#print(LVSax)

LVLax = data1[Globewhere[4,0]]
LVLax = LVLax.tolist()
del LVLax[0:2]
#print(LVLax)

LV3D = data1[Globewhere[5,0]]
LV3D = LV3D.tolist()
del LV3D[0:2]
#print(LV3D)

#Radial, Circum, Long,ms,ms,ms,RR,CR,LR,j,j,j,mm,mm,mm,ms
#0,1,2,6,7,8
#Radial = 0,6
#Circum = 1,7
#Long = 2,8

#LV Results
LVLong = [0]*2
LVLong[0] = LVLax[2]
LVLong[1] = LVLax[8]

LV3DLong = [0]*2
LV3DLong[0] = LV3D[2]
LV3DLong[1] = LV3D[8]

LVCircum = [0]*2
LVCircum[0] = LVSax[1]
LVCircum[1] = LVSax[7]

LV3DCircum = [0]*2
LV3DCircum[0] = LV3D[1]
LV3DCircum[1] = LVSax[7]

LVSaxRadial = [0]*2
LVLaxRadial = [0]*2
LV3DRadial = [0]*2
LVLaxRadial[0] = LVLax[0]
LVLaxRadial[1] = LVLax[6]
LVSaxRadial[0] = LVSax[0]
LVSaxRadial[1] = LVSax[6]
LV3DRadial[0] = LV3D[0]
LV3DRadial[1] = LV3D[6]


#RV 2D Results
RVLong = [0]*2
RVLong[0] = RVLax[2]
RVLong[1] = RVLax[8]

RVCircum = [0]*2
RVCircum[0] = RVSax[1]
RVCircum[1] = RVSax[7]

RVSaxRadial = [0]*2
RVLaxRadial = [0]*2
RVLaxRadial[0] = RVLax[0]
RVLaxRadial[1] = RVLax[6]
RVSaxRadial[0] = RVSax[0]
RVSaxRadial[1] = RVSax[6]
#print("RV 2D Global Longitudinal Strain: ", RVLong)

#RV3D Located elsewhere in different format
RV3DRadial = [0]*2
RV3DRadialp = data1[Globewhere[6,0]]
RV3DRadialp = RV3DRadialp.tolist()
RV3DRadialp.pop(0)
del RV3DRadialp[20:26]
#RV3DRadial1 = np.array(RV3DRadial)
#float(RV3DRadial)
#print(RV3DRadialp)
RV3DRadialp = max(RV3DRadialp, key=float)

RV3DRadialrate = data1[Globewhere[7,0]]
RV3DRadialrate = RV3DRadialrate.tolist()
RV3DRadialrate.pop(0)
del RV3DRadialrate[20:26]
#print(RV3DRadialrate)
RV3DRadialrate = max(RV3DRadialrate, key=float)

RV3DRadial = [RV3DRadialp, RV3DRadialrate]

RV3DCircum = [0]*2

RV3DCircump = data1[Globewhere[10,0]]
RV3DCircump = RV3DCircump.tolist()
RV3DCircump.pop(0)
del RV3DCircump[20:26]
RV3DCircump = min(RV3DCircump, key=float)


RV3DCircumrate = data1[Globewhere[11,0]]
RV3DCircumrate = RV3DCircumrate.tolist()
RV3DCircumrate.pop(0)
del RV3DCircumrate[20:26]
RV3DCircumrate = min(RV3DCircumrate, key=float)

RV3DCircum = [RV3DCircump, RV3DCircumrate]

RV3DLong = [0]*2

RV3DLongp = data1[Globewhere[14,0]]
RV3DLongp = RV3DLongp.tolist()
RV3DLongp.pop(0)
del RV3DLongp[20:26]
RV3DLongp = min(RV3DLongp, key=float)

RV3DLongrate = data1[Globewhere[15,0]]
RV3DLongrate = RV3DLongrate.tolist()
RV3DLongrate.pop(0)
del RV3DLongrate[20:26]
RV3DLongrate = min(RV3DLongrate, key=float)

RV3DLong = [RV3DLongp, RV3DLongrate]


torsionwhere = np.argwhere(data1 == "torsion")
RVTorsion = data1[torsionwhere[0,0]]
RVTorsion = RVTorsion.tolist()
RVTorsion.pop(0)
del RVTorsion[20:26]
RVTorsion = max(RVTorsion, key=float)
#print(RVTorsion)

LVTorsion = data1[torsionwhere[1,0]]
LVTorsion = LVTorsion.tolist()
LVTorsion.pop(0)
#print(LVTorsion)
del LVTorsion[20:26]
LVTorsion = max(LVTorsion, key=float)

#print(LVTorsion)

patientwhere = np.argwhere(data1 == "Patient")
pnamefull = data1[patientwhere[0,0]]
pnamefull = pnamefull.tolist()
pnamefull.pop(0)
fullname = pnamefull[0]
Name = fullname.split(',')

birthdatewhere = np.argwhere(data1 == "Birth Date")
bdate = data1[birthdatewhere[0,0]]
bdate = bdate.tolist()
bdate.pop(0)

IDwhere = np.argwhere(data1 == "PatientID")
pid = data1[IDwhere[0,0]]
pid = pid.tolist()
pid.pop(0)

Sdatewhere = np.argwhere(data1 == "Study Date")
Sdate = data1[Sdatewhere[0,0]]
Sdate = Sdate.tolist()
Sdate.pop(0)

#LV Measurements
#Search: EDV, ESV, SV,HR,CO,EF,MyoMass_diast

edvwhere = np.argwhere(data1 == "EDV")
edv = data1[edvwhere[0,0]]
edv = edv.tolist()
edv.pop(0)

esvwhere = np.argwhere(data1 == "ESV")
esv = data1[esvwhere[0,0]]
esv = esv.tolist()
esv.pop(0)

svwhere = np.argwhere(data1 == "SV")
sv = data1[svwhere[0,0]]
sv = sv.tolist()
sv.pop(0)

hrwhere = np.argwhere(data1 == "HR")
hr = data1[hrwhere[0,0]]
hr = hr.tolist()
hr.pop(0)

COwhere = np.argwhere(data1 == "CO")
co = data1[COwhere[0,0]]
co = co.tolist()
co.pop(0)

EFwhere = np.argwhere(data1 == "EF")
ef = data1[EFwhere[0,0]]
ef = ef.tolist()
ef.pop(0)

LVMwhere = np.argwhere(data1 == "MyoMass_diast") 
lvm = data1[LVMwhere[0,0]]
lvm = lvm.tolist()
lvm.pop(0)

#Assemble data into single list
procdata = [Name[0], Name[1], Sdate[0], "1","Vibhav","nan", "nan", pid[0], bdate[0], 
            hr[0], edv[0], esv[0], sv[0], ef[0], co[0], lvm[0], LVLong[0], LVLong[1], 
            LV3DLong[0], LV3DLong[1], LVCircum[0], LVCircum[1], LV3DCircum[0], 
            LV3DCircum[1], LVSaxRadial[0], LVLaxRadial[0], LVSaxRadial[1], LVLaxRadial[1], 
            LV3DRadial[0], LV3DRadial[1], LVTorsion, RVLong[0], RVLong[1],RV3DLong[0], 
            RV3DLong[1], RVCircum[0], RVCircum[1], RV3DCircum[0], RV3DCircum[1], 
            RVSaxRadial[0], RVLaxRadial[0], RVSaxRadial[1], RVLaxRadial[1], RV3DRadial[0], 
            RV3DRadial[1], RVTorsion]


print(procdata)

with open("random.csv", "a", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(procdata)