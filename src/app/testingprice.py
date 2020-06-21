# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:45:13 2020

@author: NTSL6
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:43:03 2020

@author: NTSL6
"""

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
from scipy.stats import norm
import pandas as pd


#datapath = '../../data/raw/4579_Intel_CPUs.csv'
#data = pd.read_csv(datapath) 


pdDDR4 = pd.read_csv('../data/RAM_DDR43_Cleaned.csv')
HDDSDD = pd.read_csv('../data/HDDSSDclean.csv') 
CPUIntel = pd.read_csv('../data/CPUCleanedprice.csv')
CPUIntel_price = pd.read_csv('../data/CPUCleanedprice.csv')
GPU = pd.read_csv('../data/GPUprice_G3Dmark.csv')
GPU_price = pd.read_csv('../data/GPUprice_G3Dmark.csv')
coeffMark = pd.read_csv('../data/Coefficients.csv')

#%%
#st.title('PCvalueBuilder')
#st.subheader('Predicting the performance of replacement PC parts')
###################################################################
#part_avail = ['Processor','GPU','Hard Drive','RAM']
#part_1 = st.selectbox('Select Part', ['Processor','GPU','Hard Drive','RAM'])
#if part_1 == 'Processor':
#    options_1 = st.selectbox('Part 1: Processor', CPUIntel['name'])
#    CPU_Mark = CPUIntel[CPUIntel['name'] == options_1].CPUMark.tolist()[0]
#    CPU_year = CPUIntel[CPUIntel['name'] == options_1].year.tolist()[0]
#    CPU_Mark_p = CPUIntel_price[CPUIntel_price['name'] == options_1].CPUMark.tolist()[0]/CPUIntel_price[CPUIntel_price['name'] == options_1].price.tolist()[0]
#elif part_1 == 'GPU':
#    options_1 = st.selectbox('Part 1: GPU', GPU['name'])
#    GPU_Mark = GPU[GPU['name'] == options_1].G3DMark.tolist()[0]
#    GPU_Mark_p = GPU_price[GPU_price['name'] == options_1].G3DMark.tolist()[0]/GPU_price[GPU_price['name'] == options_1].price.tolist()[0]
#    GPU_year = GPU[GPU['name'] == options_1].year.tolist()[0]
#elif part_1 == 'Hard Drive':
#    options_1 = st.selectbox('Part 1: Hard Drive', HDDSDD['name'])
#    Hard_Mark = HDDSDD[HDDSDD['name'] == options_1].HardMark.tolist()[0]
#    Hard_Mark_year = HDDSDD[HDDSDD['name'] == options_1].year.tolist()[0]
#    Hard_Mark_p = HDDSDD[HDDSDD['name'] == options_1].HardMark.tolist()[0]/HDDSDD[HDDSDD['name'] == options_1].price.tolist()[0]
#elif part_1 == 'RAM':
#    options_1 = st.selectbox('Part 1: RAM', pdDDR4['name'])
#    RAM_Mark = pdDDR4[pdDDR4['name'] == options_1].RAMmark.tolist()[0]
#    RAM_Mark_p = pdDDR4[pdDDR4['name'] == options_1].RAMmark.tolist()[0]/pdDDR4[pdDDR4['name'] == options_1].Price.tolist()[0]
#
###################################################################
#part2_specs = ['GPU','Hard Drive','RAM','Processor']
#part_2 = st.selectbox('Select Part 2', part2_specs)
#if part_2 == 'Processor':
#    options_2 = st.selectbox('Part 2: Processor', CPUIntel['name'])
#    CPU_Mark = CPUIntel[CPUIntel['name'] == options_2].CPUMark.tolist()[0]
#    CPU_year = CPUIntel[CPUIntel['name'] == options_2].year.tolist()[0]
#    CPU_Mark_p = CPUIntel_price[CPUIntel_price['name'] == options_2].CPUMark.tolist()[0]/CPUIntel_price[CPUIntel_price['name'] == options_2].price.tolist()[0]
#elif part_2 == 'GPU':
#    options_2 = st.selectbox('Part 2: GPU', GPU['name'])
#    GPU_Mark = GPU[GPU['name'] == options_2].G3DMark.tolist()[0]
#    GPU_Mark_p = GPU_price[GPU_price['name'] == options_2].G3DMark.tolist()[0]/GPU_price[GPU_price['name'] == options_2].price.tolist()[0]
#    GPU_year = GPU[GPU['name'] == options_2].year.tolist()[0]
#elif part_2 == 'Hard Drive':
#    options_2 = st.selectbox('Part 2: Hard Drive', HDDSDD['name'])
#    Hard_Mark = HDDSDD[HDDSDD['name'] == options_2].HardMark.tolist()[0]
#    Hard_Mark_year = HDDSDD[HDDSDD['name'] == options_2].year.tolist()[0]
#    Hard_Mark_p = HDDSDD[HDDSDD['name'] == options_2].HardMark.tolist()[0]/HDDSDD[HDDSDD['name'] == options_2].price.tolist()[0]
#elif part_2 == 'RAM':
#    options_2 = st.selectbox('Part 2: RAM', pdDDR4['name'])
#    RAM_Mark = pdDDR4[pdDDR4['name'] == options_2].RAMmark.tolist()[0]
#    RAM_Mark_p = pdDDR4[pdDDR4['name'] == options_2].RAMmark.tolist()[0]/pdDDR4[pdDDR4['name'] == options_2].Price.tolist()[0]
#
###################################################################
#part3_specs = ['RAM','Processor','GPU','Hard Drive',]
#part_3 = st.selectbox('Select Part 3', part3_specs)
#if part_3 == 'Processor':
#    options_3 = st.selectbox('Part 3: Processor', CPUIntel['name'])
#    CPU_Mark = CPUIntel[CPUIntel['name'] == options_3].CPUMark.tolist()[0]
#    CPU_year = CPUIntel[CPUIntel['name'] == options_3].year.tolist()[0]
#    CPU_Mark_p = CPUIntel_price[CPUIntel_price['name'] == options_3].CPUMark.tolist()[0]/CPUIntel_price[CPUIntel_price['name'] == options_3].price.tolist()[0]
#elif part_3 == 'GPU':
#    options_3 = st.selectbox('Part 3: GPU', GPU['name'])
#    GPU_Mark = GPU[GPU['name'] == options_3].G3DMark.tolist()[0]
#    GPU_Mark_p = GPU_price[GPU_price['name'] == options_3].G3DMark.tolist()[0]/GPU_price[GPU_price['name'] == options_3].price.tolist()[0]
#    GPU_year = GPU[GPU['name'] == options_3].year.tolist()[0]
#elif part_3 == 'Hard Drive':
#    options_3 = st.selectbox('Part 3: Hard Drive', HDDSDD['name'])
#    Hard_Mark = HDDSDD[HDDSDD['name'] == options_3].HardMark.tolist()[0]
#    Hard_Mark_year = HDDSDD[HDDSDD['name'] == options_3].year.tolist()[0]
#    Hard_Mark_p = HDDSDD[HDDSDD['name'] == options_3].HardMark.tolist()[0]/HDDSDD[HDDSDD['name'] == options_3].price.tolist()[0]
#elif part_3 == 'RAM':
#    options_3 = st.selectbox('Part 3: RAM', pdDDR4['name'])
#    RAM_Mark = pdDDR4[pdDDR4['name'] == options_3].RAMmark.tolist()[0]
#    RAM_Mark_p = pdDDR4[pdDDR4['name'] == options_3].RAMmark.tolist()[0]/pdDDR4[pdDDR4['name'] == options_3].Price.tolist()[0]
#
###################################################################
##part_options.pop(part_options.index(part_1))
##part_options.pop(part_options.index(part_2))
##part_options.pop(part_options.index(part_3))
#parts_select = [part_1,part_2,part_3]
#part_options = []
#for i in part_avail:
#    if i not in parts_select:
#        part_options.append(i)

#age = ((['Processor','GPU','Hard Drive','RAM'].remove(part_1)).remove(part_2)).remove(part_3)
#options_pref = st.selectbox('Preference', ['Value','Performance'])

GPU_Mark = GPU.iloc[0]['G3DMark']
GPU_Mark_p = GPU_Mark
GPU_year = GPU.iloc[0]['year']

RAM_Mark = pdDDR4.iloc[274]['RAMmark']
RAM_Mark_p = RAM_Mark
Hard_Mark = HDDSDD.iloc[100]['HardMark']
Hard_Mark_p = Hard_Mark
CPU_Mark = CPUIntel.iloc[494]['CPUMark']
CPU_year = CPUIntel.iloc[494]['year']
CPU_Mark_p = CPU_Mark

options_pref = 'Value'
part_options = ['GPU']

#age = st.slider('How old are you?', 0, 130, 25)
#st.write("I'm ", age, 'years old')
if len(part_options) == 1:
    st.write("Showing", part_options[0], 'options with best',options_pref )
    if part_options[0] == 'Processor':
        if options_pref == 'Performance':
            otherMark = (GPU_Mark*coeffMark.GPU_coeff[0])+(RAM_Mark*coeffMark.RAM_coeff[0])+(Hard_Mark*coeffMark.HDD_coeff[0])
            if GPU_year >= 2018:
                maxyear = 2020
                minyear = 2016
            elif GPU_year <= 2015:
                maxyear = 2018
                minyear = 2015
            else:
                maxyear = GPU_year+2
                minyear = GPU_year-2
            CPU_data = CPUIntel[(CPUIntel['year']<=maxyear) & (CPUIntel['year']>=minyear)]
            CPU_Mark = np.array(CPU_data.CPUMark.tolist())*coeffMark.CPU_coeff[0]
            sysScore = ((otherMark+CPU_Mark)/5.0)
            indices = np.argsort(sysScore)
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    result = pd.concat([result,(pd.Series([CPU_data.iloc[indices[-(i+1)]]['name'], int(sysScore[indices[-(i+1)]]), int(sysScore[indices[-1]]/np.array(CPU_data.iloc[indices[-(i+1)]]['price'])),CPU_data.iloc[indices[-(i+1)]]['price']]))],ignore_index=True)
                else:
                    result = pd.concat([result,(pd.Series([CPU_data.iloc[indices[-(i+1)]]['name'], int(sysScore[indices[-(i+1)]]), int(sysScore[indices[-1]]/np.array(CPU_data.iloc[indices[-(i+1)]]['price'])),CPU_data.iloc[indices[-(i+1)]]['price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] + " name", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)

        elif options_pref == 'Value':
            otherMark = (GPU_Mark_p*coeffMark.GPU_coeff[0])+(RAM_Mark_p*coeffMark.RAM_coeff[0])+(Hard_Mark_p*coeffMark.HDD_coeff[0])
            if GPU_year >= 2018:
                maxyear = 2020
                minyear = 2016
            elif GPU_year <= 2015:
                maxyear = 2018
                minyear = 2015
            else:
                maxyear = GPU_year+2
                minyear = GPU_year-2
            CPU_data = CPUIntel[(CPUIntel['year']<=maxyear) & (CPUIntel['year']>=minyear)]
            CPU_Mark = np.array(CPU_data.CPUMark.tolist())*coeffMark.CPU_coeff[0]
            CPU_Mark_p = (np.array(CPU_data.CPUMark.tolist())/np.array(CPU_data.price.tolist()))*coeffMark.CPU_coeff[0]
            sysScore = ((otherMark+CPU_Mark_p)/5.0)
            valueScore = ((otherMark+CPU_Mark)/5.0)/np.array(CPU_data.price.tolist())
            indices = np.argsort(sysScore)
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    result = pd.concat([result,(pd.Series([CPU_data.iloc[indices[-(i+1)]]['name'], int(CPU_data.iloc[indices[-(i+1)]]['CPUMark']), int(valueScore[indices[-(i+1)]]), CPU_data.iloc[indices[-(i+1)]]['price']]))],ignore_index=True)
                else:
                    result = pd.concat([result,(pd.Series([CPU_data.iloc[indices[-(i+1)]]['name'], int(CPU_data.iloc[indices[-(i+1)]]['CPUMark']), int(valueScore[indices[-(i+1)]]), CPU_data.iloc[indices[-(i+1)]]['price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] + " name", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)

    
    elif part_options[0] == 'GPU':
        if CPU_year >= 2018:
            maxyear = 2020
            minyear = 2016
        elif CPU_year <= 2015:
            maxyear = 2018
            minyear = 2015
        else:
            maxyear = CPU_year+2
            minyear = CPU_year-2
        if options_pref == 'Performance':
            otherMark = (RAM_Mark*coeffMark.RAM_coeff[0])+(Hard_Mark*coeffMark.HDD_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
            GPU_Mark = np.array(GPU.G3DMark.tolist())*coeffMark.GPU_coeff[0]
            sysScore = ((otherMark+GPU_Mark)/5.0)
            indices = np.argsort(sysScore)
            
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    result = pd.concat([result,(pd.Series([GPU.iloc[indices[-(i+1)]]['name'], int(sysScore[indices[-(i+1)]]), int(sysScore[indices[-1]]/np.array(GPU.iloc[indices[-(i+1)]]['price'])),GPU.iloc[indices[-(i+1)]]['price']]))],ignore_index=True)
                else:
                    result = pd.concat([result,(pd.Series([GPU.iloc[indices[-(i+1)]]['name'], int(sysScore[indices[-(i+1)]]), int(sysScore[indices[-1]]/np.array(GPU.iloc[indices[-(i+1)]]['price'])),GPU.iloc[indices[-(i+1)]]['price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] +" name", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)
            
            
        elif options_pref == 'Value':
            otherMark_p = (RAM_Mark_p*coeffMark.RAM_coeff[0])+(Hard_Mark_p*coeffMark.HDD_coeff[0])+(CPU_Mark_p*coeffMark.CPU_coeff[0])
            otherMark = (RAM_Mark*coeffMark.RAM_coeff[0])+(Hard_Mark*coeffMark.HDD_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
            GPU_Mark = np.array(GPU.G3DMark.tolist())*coeffMark.GPU_coeff[0]
            GPU_Mark_p = (np.array(GPU.G3DMark.tolist())/np.array(GPU.price.tolist()))*coeffMark.GPU_coeff[0]
            sysScore = ((otherMark_p+GPU_Mark_p)/5.0)
            valueScore = ((otherMark+GPU_Mark)/5.0)/np.array(GPU.price.tolist())
            mu, std = norm.fit(sysScore)
            
            sysScore_perf = ((otherMark+GPU_Mark)/5.0)
            mu_perf, std_perf = norm.fit(sysScore_perf)
            indices = np.argsort(sysScore)
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    result = pd.concat([result,(pd.Series([GPU_price.iloc[indices[-(i+1)]]['name'], int(GPU_price.iloc[indices[-(i+1)]]['G3DMark']), int(sysScore[indices[-(i+1)]]), GPU_price.iloc[indices[-(i+1)]]['price']]))],ignore_index=True)
                else:
                    result = pd.concat([result,(pd.Series([GPU_price.iloc[indices[-(i+1)]]['name'], int(GPU_price.iloc[indices[-(i+1)]]['G3DMark']), int(sysScore[indices[-(i+1)]]), GPU_price.iloc[indices[-(i+1)]]['price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] + " name", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)
            
            
    elif part_options[0] == 'Hard Drive':
        if CPU_year >= 2018:
            maxyear = 2020
            minyear = 2016
        elif CPU_year <= 2015:
            maxyear = 2018
            minyear = 2015
        else:
            maxyear = CPU_year+2
            minyear = CPU_year-2
        if options_pref == 'Performance':
            otherMark = (RAM_Mark*coeffMark.RAM_coeff[0])+(GPU_Mark*coeffMark.GPU_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
            HDD_data = HDDSDD[(HDDSDD['year']<=maxyear) & (HDDSDD['year']>=minyear)]
            Hard_Mark = np.array(HDD_data.HardMark.tolist())*coeffMark.HDD_coeff[0]
            sysScore = ((otherMark+Hard_Mark)/5.0)
            indices = np.argsort(sysScore)
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    sizeHDD = float(HDDSDD.iloc[indices[-(i+1)]]['size'])
                    if sizeHDD < 10:
                        sizeHDD = str(sizeHDD) + ' TB'
                    else:
                        sizeHDD = str(sizeHDD) + ' GB'
                    result = pd.concat([result,(pd.Series([HDDSDD.iloc[indices[-(i+1)]]['name'],  sizeHDD ,int(sysScore[indices[-(i+1)]]), int(HDDSDD.iloc[indices[-(i+1)]]['HardMark']/np.array(HDDSDD.iloc[indices[-(i+1)]]['price'])),HDDSDD.iloc[indices[-(i+1)]]['price']]))],ignore_index=True)
                else:
                    sizeHDD = float(HDDSDD.iloc[indices[-(i+1)]]['size'])
                    if sizeHDD < 10:
                        sizeHDD = str(sizeHDD) + ' TB'
                    else:
                        sizeHDD = str(sizeHDD) + ' GB'
                    result = pd.concat([result,(pd.Series([HDDSDD.iloc[indices[-(i+1)]]['name'],  sizeHDD ,int(sysScore[indices[-(i+1)]]), int(HDDSDD.iloc[indices[-(i+1)]]['HardMark']/np.array(HDDSDD.iloc[indices[-(i+1)]]['price'])),HDDSDD.iloc[indices[-(i+1)]]['price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] +" name", "Size" ,"Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)
            
            
            
        elif options_pref == 'Value':
            otherMark = (RAM_Mark_p*coeffMark.RAM_coeff[0])+(GPU_Mark_p*coeffMark.GPU_coeff[0])+(CPU_Mark_p*coeffMark.CPU_coeff[0])
            HDD_data = HDDSDD[(HDDSDD['year']<=maxyear) & (HDDSDD['year']>=minyear)]
            Hard_Mark = np.array(HDD_data.HardMark.tolist())*coeffMark.HDD_coeff[0]
            Hard_Mark_p = (np.array(HDD_data.HardMark.tolist())/np.array(HDD_data.price.tolist()))*coeffMark.HDD_coeff[0]
            sysScore = ((otherMark+Hard_Mark_p)/5.0)
            valueScore = ((otherMark+Hard_Mark)/5.0)/np.array(HDD_data.price.tolist())
            indices = np.argsort(sysScore)
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    sizeHDD = float(HDDSDD.iloc[indices[-(i+1)]]['size'])
                    if sizeHDD < 10:
                        sizeHDD = str(sizeHDD) + ' TB'
                    else:
                        sizeHDD = str(sizeHDD) + ' GB'
                    result = pd.concat([result,(pd.Series([HDDSDD.iloc[indices[-(i+1)]]['name'], sizeHDD ,int(HDDSDD.iloc[indices[-(i+1)]]['HardMark']), int(HDDSDD.iloc[indices[-(i+1)]]['HardMark']/np.array(HDDSDD.iloc[indices[-(i+1)]]['price'])), HDDSDD.iloc[indices[-(i+1)]]['price']]))],ignore_index=True)
                else:
                    sizeHDD = float(HDDSDD.iloc[indices[-(i+1)]]['size'])
                    if sizeHDD < 10:
                        sizeHDD = str(sizeHDD) + ' TB'
                    else:
                        sizeHDD = str(sizeHDD) + ' GB'
                    result = pd.concat([result,(pd.Series([HDDSDD.iloc[indices[-(i+1)]]['name'], sizeHDD , int(HDDSDD.iloc[indices[-(i+1)]]['HardMark']), int(HDDSDD.iloc[indices[-(i+1)]]['HardMark']/np.array(HDDSDD.iloc[indices[-(i+1)]]['price'])), HDDSDD.iloc[indices[-(i+1)]]['price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] + " name", "Size", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)
            
            
    elif part_options[0] == 'RAM':
        if CPU_year > 2014:
            RAM_data = pdDDR4[pdDDR4['DDR3_4'] == 1]
        else:
            RAM_data = pdDDR4[pdDDR4['DDR3_4'] == 0]
        if options_pref == 'Performance':
            otherMark = (Hard_Mark*coeffMark.HDD_coeff[0])+(GPU_Mark*coeffMark.GPU_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
            RAM_Mark = np.array(RAM_data.RAMmark.tolist())*coeffMark.RAM_coeff[0]
            sysScore = ((otherMark+RAM_Mark)/5.0)
            indices = np.argsort(sysScore)
            
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    sizeHDD = str(RAM_data.iloc[indices[-(i+1)]]['size'])+ ' GB'                    
                    result = pd.concat([result,(pd.Series([RAM_data.iloc[indices[-(i+1)]]['name'], sizeHDD ,int(sysScore[indices[-(i+1)]]), int(sysScore[indices[-(i+1)]]/np.array(RAM_data.iloc[indices[-(i+1)]]['Price'])), RAM_data.iloc[indices[-(i+1)]]['Price']]))],ignore_index=True)
                else:
                    sizeHDD = str(RAM_data.iloc[indices[-(i+1)]]['size'])+ ' GB'
                    result = pd.concat([result,(pd.Series([RAM_data.iloc[indices[-(i+1)]]['name'], sizeHDD , int(sysScore[indices[-(i+1)]]), int(sysScore[indices[-(i+1)]]/np.array(RAM_data.iloc[indices[-(i+1)]]['Price'])), RAM_data.iloc[indices[-(i+1)]]['Price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] + " name", "Size", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)
            
            
        elif options_pref == 'Value':
            otherMark = (Hard_Mark_p*coeffMark.HDD_coeff[0])+(GPU_Mark_p*coeffMark.GPU_coeff[0])+(CPU_Mark_p*coeffMark.CPU_coeff[0])
            RAM_Mark = np.array(RAM_data.RAMmark.tolist())*coeffMark.RAM_coeff[0]
            RAM_Mark_p = (np.array(RAM_data.RAMmark.tolist())/np.array(RAM_data.Price.tolist()))*coeffMark.RAM_coeff[0]
            sysScore = ((otherMark+RAM_Mark_p)/5.0)
            valueScore = ((otherMark+RAM_Mark)/5.0)/np.array(RAM_data.price.tolist())
            indices = np.argsort(sysScore)
            
            result = pd.DataFrame()
            for i in range(5):
                if i == 0:
                    sizeHDD = str(RAM_data.iloc[indices[-(i+1)]]['size'])+ ' GB'                    
                    result = pd.concat([result,(pd.Series([RAM_data.iloc[indices[-(i+1)]]['name'], sizeHDD ,int(RAM_data.iloc[indices[-(i+1)]]['RAMmark']), int(valueScore[indices[-(i+1)]]), RAM_data.iloc[indices[-(i+1)]]['Price']]))],ignore_index=True)
                else:
                    sizeHDD = str(RAM_data.iloc[indices[-(i+1)]]['size'])+ ' GB'
                    result = pd.concat([result,(pd.Series([RAM_data.iloc[indices[-(i+1)]]['name'], sizeHDD , int(RAM_data.iloc[indices[-(i+1)]]['RAMmark']), int(valueScore[indices[-(i+1)]]), RAM_data.iloc[indices[-(i+1)]]['Price']]))], axis=1,ignore_index=True)
            result.index = [part_options[0] + " name", "Size", "Performance score", "Value Score(/$)", "Price"]
            result= result.T
            result.index = ["1","2","3","4","5"]
            #st.table(result)
            
            
#else:
    #st.subheader("Please select three unique parts from Processor, GPU, RAM and Hard drive.")




