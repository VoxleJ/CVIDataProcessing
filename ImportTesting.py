# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 12:54:45 2019

@author: vjha1
"""
#import numpy as np
import csv


with open("filename.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]


patient = data[3]
PatientName = patient[1]
print('Name: ', PatientName)

birthdate = data[4]
birthdate = birthdate[1]
print('Birthdate: ', birthdate)

patientID = data[5]
patientID = patientID[1]
print('FHS ID: ', patientID)

studydate = data[7]
studydate = studydate[1]
print('Study Date: ', studydate)

