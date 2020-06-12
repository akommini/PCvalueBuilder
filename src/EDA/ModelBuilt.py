# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:00:57 2020

@author: NTSL6
"""

import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import plotly


pdDDR3 = pd.read_csv('../RAM/DDR3Cleaned.csv')
pdDDR4 = pd.read_csv('../RAM/DDR4Cleaned.csv')
HDDSDD = pd.read_csv('../HardDrive/hardDriveCleaned.csv') 
CPUIntel = pd.read_csv('../Processor/Clean/CPUCleanedIntel.csv')
GPU = pd.read_csv('../GPU/cleaned/GPUCleaned.csv')


CPU_Mark = np.array(CPUIntel.CPUMark.tolist())
CPU_Mark_p = (np.array(CPUIntel.CPUMark.tolist())/np.array(CPUIntel.price.tolist()))

GPU_Mark = np.array(GPU.G3DMark.tolist())
GPU_Mark_p = (np.array(GPU.G3DMark.tolist())/np.array(GPU.price.tolist()))

Hard_Mark = np.array(HDDSDD.HardMark.tolist())
Hard_Mark_p = (np.array(HDDSDD.HardMark.tolist())/np.array(HDDSDD.price.tolist()))

RAM_Mark = np.array(pdDDR4.RAMmark.tolist())
RAM_Mark_p = (np.array(pdDDR4.RAMmark.tolist())/np.array(pdDDR4.Price.tolist()))


fig, ax = plt.subplots(figsize=(11,8))

#ax.scatter(np.array(CPUIntel.year.tolist()), CPU_Mark/np.amax(CPU_Mark), c='brown', alpha=0.4, edgecolors='none')
#ax.scatter(np.array(CPUIntel.year.tolist()), CPU_Mark_p/np.amax(CPU_Mark_p), c='green', alpha=0.4, edgecolors='none')

#ax.scatter(np.array(GPU.year.tolist()), GPU_Mark/np.amax(GPU_Mark), c='brown', alpha=0.4, edgecolors='none')
ax.scatter(np.array(GPU.year.tolist()), GPU_Mark_p/np.amax(GPU_Mark_p), c='green', alpha=0.4, edgecolors='none')


#plt.title('Processor',fontsize=28)
plt.title('Graphics Card',fontsize=28)
plt.xlabel('Year',fontsize=18)
plt.ylabel('Normalized Score (Value)',fontsize=18)
#plt.ylabel('Normalized Score (Performance)',fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
