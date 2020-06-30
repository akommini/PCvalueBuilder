# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:37:37 2020

@author: NTSL6
"""

import numpy as np
import pandas as pd
import math

def dateEx(value):
    out = value.split('-')
    if out[0].isdigit():
        if len(out[0]) == 1:
            out = '200' + out[0]
        elif len(out[0]) == 2:
            out = '20' + out[0]
    elif out[1].isdigit():
        out = '20' + out[1]
    return out

def priceStrip(value):
    if value[0] == '$' and value[-1] == '*':
        temp = value[1:-2]
        if len(temp.split(','))>1:
            out = float(temp.split(',')[0]+temp.split(',')[1])
        else:
            out = float(temp)
    elif value[0] == '$' and value[-1] != '*':
        temp = value[1:]  
        if len(temp.split(','))>1:
            out = float(temp.split(',')[0]+temp.split(',')[1])
        else:
            out = float(temp)
    return out

############################################
#datapath = pd.read_csv('datasetsGPUspecs.csv')
datapath = pd.read_csv('cputableGPU.csv')
#fpassMark = open('cputableGPU.csv')
#CPUdataPath = open('datasetsGPUspecs.csv')
############################################


#FeatureData = datapath[datapath['Price1'].notna()]
#FeatureData=FeatureData.fillna(-1)
FeatureData=datapath.fillna(-1)


col_names =  ['name','year','TDP','price','G3DMark','G2DMark']
my_df  = pd.DataFrame(columns = col_names)

for i in FeatureData['Videocard_Name']:
    x = FeatureData[FeatureData['Videocard_Name']==i]
    Name = (x.Videocard_Name).tolist()[0]
    year = dateEx((x.Test_Date5).tolist()[0])
    TDP = float(x.TDP.tolist()[0])
    if x.Price1.tolist()[0] == -1:
        Price = 0
    else:
        Price = priceStrip(x.Price1.tolist()[0])
    G3D_Mark = float(x.G3D_Mark.tolist()[0])
    G2D_Mark = float(x.G2D_Mark.tolist()[0])
    rowDf = [Name,year,TDP,Price,G3D_Mark,G2D_Mark]
    my_df.loc[len(my_df)] = rowDf
    
my_df.to_csv('GPUprice_G3Dmark_full.csv')  