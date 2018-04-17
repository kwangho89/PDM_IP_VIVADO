# -*- coding: utf-8 -*-
"""
PDM IP MAKING USIG VIVADO & PYTHON
Editor: KWANGDALF
"""

import numpy as np;
import matplotlib.pyplot as plt;
import csv;

freq_a = 10000;   #frequency for Acoustic wave
freq_s = 2.5e6;    #frequency for Sampling

samples=500;        # number of Samples
t_test = np.arange(samples);  #time array

y_a=np.sin(2*np.pi*freq_a/freq_s*t_test);   #analog signal
y_d=np.zeros(samples);      #array for PDM signals converted using a first-order sigma-delta modulator

"""
https://en.wikipedia.org/wiki/Pulse-density_modulation

Encode samples into pulse-density modulation
using a first-order sigma-delta modulator
"""

eq=0;
for i in range(y_a.size):
    if y_a[i]>=eq:
        y_d[i]=1
    else:
        y_d[i]=-1
    eq=y_d[i]-y_a[i]+eq;
    
"""
matplot tutorial
https://matplotlib.org/users/pyplot_tutorial.html
"""
plt.figure(1)
plt.subplot(211)
plt.plot(t_test/freq_s,y_a,'b.')
plt.subplot(212)
plt.plot(t_test/freq_s,y_d,'r-')
plt.show()

"""
CSV Writer
https://docs.python.org/3/library/csv.html
http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
"""

with open('analog.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(y_a.size):
        writer.writerow([i/freq_s,y_a[i]])
f.close()        

with open('PDM.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(y_d.size):
        writer.writerow([i/freq_s,y_d[i]])
f.close()