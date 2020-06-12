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


pdDDR4 = pd.read_csv('../data/RAM_DDR43_Cleaned.csv')
HDDSDD = pd.read_csv('../data/HDDSSDclean.csv') 
CPUIntel = pd.read_csv('../data/CPUCleanedprice.csv')
CPUIntel_price = pd.read_csv('../data/CPUCleanedprice.csv')
GPU = pd.read_csv('../data/GPUprice_G3Dmark.csv')
GPU_price = pd.read_csv('../data/GPUprice_G3Dmark.csv')
coeffMark = pd.read_csv('../data/Coefficients.csv')

st.title('PCvalueBuilder')
st.subheader('Predicting the performance of replacement PC parts')
##################################################################
part_options = ['Processor','GPU','Hard Drive','RAM']
part_1 = st.selectbox('Select Part', ['Processor','GPU','Hard Drive','RAM'])
if part_1 == 'Processor':
    options_1 = st.selectbox('Processor', CPUIntel['name'])
    CPU_Mark = CPUIntel[CPUIntel['name'] == options_1].CPUMark.tolist()[0]
    CPU_Mark_p = CPUIntel_price[CPUIntel_price['name'] == options_1].CPUMark.tolist()[0]/CPUIntel_price[CPUIntel_price['name'] == options_1].price.tolist()[0]
elif part_1 == 'GPU':
    options_1 = st.selectbox('GPU', GPU['name'])
    GPU_Mark = GPU[GPU['name'] == options_1].G3DMark.tolist()[0]
    GPU_Mark_p = GPU_price[GPU_price['name'] == options_1].G3DMark.tolist()[0]/GPU_price[GPU_price['name'] == options_1].price.tolist()[0]
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
part2_specs = ['GPU','Hard Drive','RAM','Processor']
part_2 = st.selectbox('Select Part 2', part2_specs)
if part_2 == 'Processor':
    options_2 = st.selectbox('Part 2: Processor', CPUIntel['name'])
    CPU_Mark = CPUIntel[CPUIntel['name'] == options_2].CPUMark.tolist()[0]
    CPU_Mark_p = CPUIntel_price[CPUIntel_price['name'] == options_2].CPUMark.tolist()[0]/CPUIntel_price[CPUIntel_price['name'] == options_2].price.tolist()[0]
elif part_2 == 'GPU':
    options_2 = st.selectbox('Part 2: GPU', GPU['name'])
    GPU_Mark = GPU[GPU['name'] == options_2].G3DMark.tolist()[0]
    GPU_Mark_p = GPU_price[GPU_price['name'] == options_2].G3DMark.tolist()[0]/GPU_price[GPU_price['name'] == options_2].price.tolist()[0]
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
part3_specs = ['RAM','Processor','GPU','Hard Drive',]
part_3 = st.selectbox('Select Part 3', part3_specs)
if part_3 == 'Processor':
    options_3 = st.selectbox('Part 3: Processor', CPUIntel['name'])
    CPU_Mark = CPUIntel[CPUIntel['name'] == options_3].CPUMark.tolist()[0]
    CPU_Mark_p = CPUIntel_price[CPUIntel_price['name'] == options_3].CPUMark.tolist()[0]/CPUIntel_price[CPUIntel_price['name'] == options_3].price.tolist()[0]
elif part_3 == 'GPU':
    options_3 = st.selectbox('Part 3: GPU', GPU['name'])
    GPU_Mark = GPU[GPU['name'] == options_3].G3DMark.tolist()[0]
    GPU_Mark_p = GPU_price[GPU_price['name'] == options_3].G3DMark.tolist()[0]/GPU_price[GPU_price['name'] == options_3].price.tolist()[0]
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
        GPU_year = GPU[GPU['name'] == options_3].year[0]
        otherMark = (GPU_Mark*coeffMark.GPU_coeff[0])+(RAM_Mark*coeffMark.RAM_coeff[0])+(Hard_Mark*coeffMark.HDD_coeff[0])
        CPU_data = CPUIntel[CPUIntel['year']]
        CPU_Mark = np.array(CPUIntel.CPUMark.tolist())*coeffMark.CPU_coeff[0]
        sysScore = ((otherMark+CPU_Mark)/5.0)
        indices = np.argsort(sysScore)
        st.write("1. ", CPUIntel.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
        st.write("2. ", CPUIntel.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
        st.write("3. ", CPUIntel.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
        st.write("4. ", CPUIntel.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
        st.write("5. ", CPUIntel.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])
    elif options_pref == 'Value':
        otherMark = (GPU_Mark_p*coeffMark.GPU_coeff[0])+(RAM_Mark_p*coeffMark.RAM_coeff[0])+(Hard_Mark_p*coeffMark.HDD_coeff[0])
        CPU_Mark_p = (np.array(CPUIntel_price.CPUMark.tolist())/np.array(CPUIntel_price.price.tolist()))*coeffMark.CPU_coeff[0]
        sysScore = ((otherMark+CPU_Mark_p)/5.0)
        indices = np.argsort(sysScore)
        st.write("1. ", CPUIntel_price.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
        st.write("2. ", CPUIntel_price.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
        st.write("3. ", CPUIntel_price.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
        st.write("4. ", CPUIntel_price.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
        st.write("5. ", CPUIntel_price.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])

elif part_options[0] == 'GPU':
    if options_pref == 'Performance':
        otherMark = (RAM_Mark*coeffMark.RAM_coeff[0])+(Hard_Mark*coeffMark.HDD_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
        GPU_Mark = np.array(GPU.G3DMark.tolist())*coeffMark.GPU_coeff[0]
        sysScore = ((otherMark+GPU_Mark)/5.0)
        indices = np.argsort(sysScore)
        st.write("1.", GPU.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
        st.write("2.", GPU.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
        st.write("3.", GPU.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
        st.write("4.", GPU.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
        st.write("5.", GPU.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])
    elif options_pref == 'Value':
        otherMark = (RAM_Mark_p*coeffMark.RAM_coeff[0])+(Hard_Mark_p*coeffMark.HDD_coeff[0])+(CPU_Mark_p*coeffMark.CPU_coeff[0])
        GPU_Mark_p = (np.array(GPU.G3DMark.tolist())/np.array(GPU.price.tolist()))*coeffMark.GPU_coeff[0]
        sysScore = ((otherMark+GPU_Mark_p)/5.0)
        indices = np.argsort(sysScore)
        st.write("1.", GPU_price.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
        st.write("2.", GPU_price.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
        st.write("3.", GPU_price.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
        st.write("4.", GPU_price.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
        st.write("5.", GPU_price.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])
elif part_options[0] == 'Hard Drive':
    if options_pref == 'Performance':
        otherMark = (RAM_Mark*coeffMark.RAM_coeff[0])+(GPU_Mark*coeffMark.GPU_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
        Hard_Mark = np.array(HDDSDD.HardMark.tolist())*coeffMark.HDD_coeff[0]
        sysScore = ((otherMark+Hard_Mark)/5.0)
        indices = np.argsort(sysScore)
    elif options_pref == 'Value':
        otherMark = (RAM_Mark_p*coeffMark.RAM_coeff[0])+(GPU_Mark_p*coeffMark.GPU_coeff[0])+(CPU_Mark_p*coeffMark.CPU_coeff[0])
        Hard_Mark_p = (np.array(HDDSDD.HardMark.tolist())/np.array(HDDSDD.price.tolist()))*coeffMark.HDD_coeff[0]
        sysScore = ((otherMark+Hard_Mark_p)/5.0)
        indices = np.argsort(sysScore)
    st.write("1.", HDDSDD.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
    st.write("2.", HDDSDD.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
    st.write("3.", HDDSDD.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
    st.write("4.", HDDSDD.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
    st.write("5.", HDDSDD.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])
elif part_options[0] == 'RAM':
    if options_pref == 'Performance':
        otherMark = (Hard_Mark*coeffMark.HDD_coeff[0])+(GPU_Mark*coeffMark.GPU_coeff[0])+(CPU_Mark*coeffMark.CPU_coeff[0])
        RAM_Mark = np.array(pdDDR4.RAMmark.tolist())*coeffMark.RAM_coeff[0]
        sysScore = ((otherMark+RAM_Mark)/5.0)
        indices = np.argsort(sysScore)
    elif options_pref == 'Value':
        otherMark = (Hard_Mark_p*coeffMark.HDD_coeff[0])+(GPU_Mark_p*coeffMark.GPU_coeff[0])+(CPU_Mark_p*coeffMark.CPU_coeff[0])
        RAM_Mark_p = (np.array(pdDDR4.RAMmark.tolist())/np.array(pdDDR4.Price.tolist()))*coeffMark.RAM_coeff[0]
        sysScore = ((otherMark+RAM_Mark_p)/5.0)
        indices = np.argsort(sysScore)
    st.write("1.", pdDDR4.iloc[indices[-1]]['name'],"-",sysScore[indices[-1]])
    st.write("2.", pdDDR4.iloc[indices[-2]]['name'],"-",sysScore[indices[-2]])
    st.write("3.", pdDDR4.iloc[indices[-3]]['name'],"-",sysScore[indices[-3]])
    st.write("4.", pdDDR4.iloc[indices[-4]]['name'],"-",sysScore[indices[-4]])
    st.write("5.", pdDDR4.iloc[indices[-5]]['name'],"-",sysScore[indices[-5]])




