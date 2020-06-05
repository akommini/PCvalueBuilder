# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:43:03 2020

@author: NTSL6
"""

import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


#datapath = '../../data/raw/4579_Intel_CPUs.csv'
#data = pd.read_csv(datapath) 


pdDDR3 = pd.read_csv('../data/DDR3Cleaned.csv')
pdDDR4 = pd.read_csv('../data/DDR4Cleaned.csv')
HDDSDD = pd.read_csv('../data/hardDriveCleaned.csv') 
CPUIntel = pd.read_csv('../data/CPUCleanedIntel.csv')
GPU = pd.read_csv('../data/GPUCleaned.csv')


st.title('PCvalueBuilder')
##################################################################
part_options = ['Processor','GPU','Hard Drive','RAM']
part_1 = st.selectbox('Select Part', ['Processor','GPU','Hard Drive','RAM'])
if part_1 == 'Processor':
    options_1 = st.selectbox('Intel Processor', CPUIntel['name'])
    CPU_Mark = CPUIntel[CPUIntel['name'] == options_1].CPUMark.tolist()[0]
    CPU_Mark_p = CPUIntel[CPUIntel['name'] == options_1].CPUMark.tolist()[0]/CPUIntel[CPUIntel['name'] == options_1].price.tolist()[0]
elif part_1 == 'GPU':
    options_1 = st.selectbox('GPU', GPU['Name'])
    GPU_Mark = GPU[GPU['Name'] == options_1].G3DMark.tolist()[0]
    GPU_Mark_p = GPU[GPU['Name'] == options_1].G3DMark.tolist()[0]/GPU[GPU['Name'] == options_1].price.tolist()[0]
elif part_1 == 'Hard Drive':
    options_1 = st.selectbox('Hard Drive', HDDSDD['name'])
    Hard_Mark = HDDSDD[HDDSDD['name'] == options_1].HardMark.tolist()[0]
    Hard_Mark_p = HDDSDD[HDDSDD['name'] == options_1].HardMark.tolist()[0]/HDDSDD[HDDSDD['name'] == options_1].price.tolist()[0]
elif part_1 == 'RAM':
    options_1 = st.selectbox('RAM', pdDDR4['name'])
    RAM_Mark = pdDDR4[pdDDR4['name'] == options_1].RAMmark.tolist()[0]
    RAM_Mark_p = pdDDR4[pdDDR4['name'] == options_1].RAMmark.tolist()[0]/pdDDR4[pdDDR4['name'] == options_1].Price.tolist()[0]
part_options.pop(part_options.index(part_1))
##################################################################
part2_specs = ['Processor','GPU','Hard Drive','RAM']
part_2 = st.selectbox('Select Part 2', part2_specs)
if part_2 == 'Processor':
    options_2 = st.selectbox('Part 2: Intel Processor', CPUIntel['name'])
    CPU_Mark = CPUIntel[CPUIntel['name'] == options_2].CPUMark.tolist()[0]
    CPU_Mark_p = CPUIntel[CPUIntel['name'] == options_2].CPUMark.tolist()[0]/CPUIntel[CPUIntel['name'] == options_2].price.tolist()[0]
elif part_2 == 'GPU':
    options_2 = st.selectbox('Part 2: GPU', GPU['Name'])
    GPU_Mark = GPU[GPU['Name'] == options_2].G3DMark.tolist()[0]
    GPU_Mark_p = GPU[GPU['Name'] == options_2].G3DMark.tolist()[0]/GPU[GPU['Name'] == options_2].price.tolist()[0]
elif part_2 == 'Hard Drive':
    options_2 = st.selectbox('Part 2: Hard Drive', HDDSDD['name'])
    Hard_Mark = HDDSDD[HDDSDD['name'] == options_2].HardMark.tolist()[0]
    Hard_Mark_p = HDDSDD[HDDSDD['name'] == options_2].HardMark.tolist()[0]/HDDSDD[HDDSDD['name'] == options_2].price.tolist()[0]
elif part_2 == 'RAM':
    options_2 = st.selectbox('Part 2: RAM', pdDDR4['name'])
    RAM_Mark = pdDDR4[pdDDR4['name'] == options_2].RAMmark.tolist()[0]
    RAM_Mark_p = pdDDR4[pdDDR4['name'] == options_2].RAMmark.tolist()[0]/pdDDR4[pdDDR4['name'] == options_2].Price.tolist()[0]
part_options.pop(part_options.index(part_2))
##################################################################
part3_specs = ['Processor','GPU','Hard Drive','RAM']
part_3 = st.selectbox('Select Part 3', part3_specs)
if part_3 == 'Processor':
    options_3 = st.selectbox('Part 3: Intel Processor', CPUIntel['name'])
    CPU_Mark = CPUIntel[CPUIntel['name'] == options_3].CPUMark.tolist()[0]
    CPU_Mark_p = CPUIntel[CPUIntel['name'] == options_3].CPUMark.tolist()[0]/CPUIntel[CPUIntel['name'] == options_3].price.tolist()[0]
elif part_3 == 'GPU':
    options_3 = st.selectbox('Part 3: GPU', GPU['Name'])
    GPU_Mark = GPU[GPU['Name'] == options_3].G3DMark.tolist()[0]
    GPU_Mark_p = GPU[GPU['Name'] == options_3].G3DMark.tolist()[0]/GPU[GPU['Name'] == options_3].price.tolist()[0]
elif part_3 == 'Hard Drive':
    options_3 = st.selectbox('Part 3: Hard Drive', HDDSDD['name'])
    Hard_Mark = HDDSDD[HDDSDD['name'] == options_3].HardMark.tolist()[0]
    Hard_Mark_p = HDDSDD[HDDSDD['name'] == options_3].HardMark.tolist()[0]/HDDSDD[HDDSDD['name'] == options_3].price.tolist()[0]
elif part_3 == 'RAM':
    options_3 = st.selectbox('Part 3: RAM', pdDDR4['name'])
    RAM_Mark = pdDDR4[pdDDR4['name'] == options_3].RAMmark.tolist()[0]
    RAM_Mark_p = pdDDR4[pdDDR4['name'] == options_3].RAMmark.tolist()[0]/pdDDR4[pdDDR4['name'] == options_3].Price.tolist()[0]
part_options.pop(part_options.index(part_3))
##################################################################
#age = ((['Processor','GPU','Hard Drive','RAM'].remove(part_1)).remove(part_2)).remove(part_3)
options_pref = st.selectbox('Preference', ['Value','Performance'])
st.write("Showing", part_options[0], 'options with best',options_pref )

#age = st.slider('How old are you?', 0, 130, 25)
#st.write("I'm ", age, 'years old')
if part_options[0] == 'Processor':
    if options_pref == 'Performance':
        otherMark = (GPU_Mark*3.178718116)+(RAM_Mark*2.757085479)+(Hard_Mark*1.668158805)
        CPU_Mark = np.array(CPUIntel.CPUMark.tolist())*0.396566187
        sysScore = ((otherMark+CPU_Mark)/5.0)
        indices = np.argsort(sysScore)
    elif options_pref == 'Value':
        otherMark = (GPU_Mark_p*3.178718116)+(RAM_Mark_p*2.757085479)+(Hard_Mark_p*1.668158805)
        CPU_Mark_p = (np.array(CPUIntel.CPUMark.tolist())/np.array(CPUIntel.price.tolist()))*0.396566187
        sysScore = ((otherMark+CPU_Mark_p)/5.0)
        indices = np.argsort(sysScore)
    st.write("1. Intel", CPUIntel.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
    st.write("2. Intel", CPUIntel.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
    st.write("3. Intel", CPUIntel.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
    st.write("4. Intel", CPUIntel.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
    st.write("5. Intel", CPUIntel.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])
elif part_options[0] == 'GPU':
    if options_pref == 'Performance':
        otherMark = (RAM_Mark*2.757085479)+(Hard_Mark*1.668158805)+(CPU_Mark*0.396566187)
        GPU_Mark = np.array(GPU.G3DMark.tolist())*3.178718116
        sysScore = ((otherMark+GPU_Mark)/5.0)
        indices = np.argsort(sysScore)
    elif options_pref == 'Value':
        otherMark = (RAM_Mark_p*2.757085479)+(Hard_Mark_p*1.668158805)+(CPU_Mark_p*0.396566187)
        GPU_Mark_p = (np.array(GPU.G3DMark.tolist())/np.array(GPU.price.tolist()))*3.178718116
        sysScore = ((otherMark+GPU_Mark_p)/5.0)
        indices = np.argsort(sysScore)
    st.write("1.", GPU.iloc[indices[-1]]['Name'],"-",sysScore[indices[-1]])
    st.write("2.", GPU.iloc[indices[-2]]['Name'],"-",sysScore[indices[-2]])
    st.write("3.", GPU.iloc[indices[-3]]['Name'],"-",sysScore[indices[-3]])
    st.write("4.", GPU.iloc[indices[-4]]['Name'],"-",sysScore[indices[-4]])
    st.write("5.", GPU.iloc[indices[-5]]['Name'],"-",sysScore[indices[-5]])
elif part_options[0] == 'Hard Drive':
    if options_pref == 'Performance':
        otherMark = (RAM_Mark*2.757085479)+(GPU_Mark*3.178718116)+(CPU_Mark*0.396566187)
        Hard_Mark = np.array(HDDSDD.HardMark.tolist())*1.668158805
        sysScore = ((otherMark+Hard_Mark)/5.0)
        indices = np.argsort(sysScore)
    elif options_pref == 'Value':
        otherMark = (RAM_Mark_p*2.757085479)+(GPU_Mark_p*3.178718116)+(CPU_Mark_p*0.396566187)
        Hard_Mark_p = (np.array(HDDSDD.HardMark.tolist())/np.array(HDDSDD.price.tolist()))*1.668158805
        sysScore = ((otherMark+Hard_Mark_p)/5.0)
        indices = np.argsort(sysScore)
    st.write("1.", HDDSDD.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
    st.write("2.", HDDSDD.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
    st.write("3.", HDDSDD.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
    st.write("4.", HDDSDD.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
    st.write("5.", HDDSDD.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])
elif part_options[0] == 'RAM':
    if options_pref == 'Performance':
        otherMark = (Hard_Mark*1.668158805)+(GPU_Mark*3.178718116)+(CPU_Mark*0.396566187)
        RAM_Mark = np.array(pdDDR4.RAMmark.tolist())*2.757085479
        sysScore = ((otherMark+RAM_Mark)/5.0)
        indices = np.argsort(sysScore)
    elif options_pref == 'Value':
        otherMark = (Hard_Mark_p*1.668158805)+(GPU_Mark_p*3.178718116)+(CPU_Mark_p*0.396566187)
        RAM_Mark_p = (np.array(pdDDR4.RAMmark.tolist())/np.array(pdDDR4.Price.tolist()))*2.757085479
        sysScore = ((otherMark+RAM_Mark_p)/5.0)
        indices = np.argsort(sysScore)
    st.write("1.", pdDDR4.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
    st.write("2.", pdDDR4.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
    st.write("3.", pdDDR4.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
    st.write("4.", pdDDR4.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
    st.write("5.", pdDDR4.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])




