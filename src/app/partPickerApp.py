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


datapath = '../../data/raw/4579_Intel_CPUs.csv'

data = pd.read_csv(datapath) 

st.title('PartPicker')
option = st.sidebar.selectbox('Product Collection?', data['Product_Collection'])

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')