# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:10:21 2018

@author: kWANGDALF
"""
import csv;
import numpy as np;

data = np.genfromtxt('analog.csv', delimiter=',')
t_test=data[:,0]
y_a=data[:,1]

data = np.genfromtxt('PDM.csv', delimiter=',')
t_test=data[:,0]
y_d=data[:,1]

#with open('parameter.csv','r') as f:
#    reader = csv.reader(f)
#    print(reader)

with open('parameter.csv',  'rt', encoding='UTF-8') as csvfile:
     para_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in para_reader:
         print(row)