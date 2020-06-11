# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:09:37 2020

@author: NTSL6
"""

import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



#datapath = '../../data/raw/4579_Intel_CPUs.csv'
#data = pd.read_csv(datapath) 

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


pdDDR3 = pd.read_csv('../data/DDR3Cleaned.csv')
pdDDR4 = pd.read_csv('../data/DDR4Cleaned.csv')
HDDSDD = pd.read_csv('../data/hardDriveCleaned.csv') 
CPUIntel = pd.read_csv('../data/CPUCleanedIntel.csv')
GPU = pd.read_csv('../data/GPUCleaned.csv')







app.layout = html.Div(children=[
    html.H1(children='PCvalueBuilder', style={
                                    'width': '60%',
                                    'margin-left': 'auto',
                                    'margin-right': 'auto',
                                    'backgroundColor': 'rgb(194, 225, 255)',}),

    html.H4(children='''
        Predicting the performance of replacement PC parts.
    ''', style={
        'width': '60%',
        'margin-left': 'auto',
        'margin-right': 'auto'}),

#    dcc.Graph(
#        id='example-graph',
#        figure={
#            'data': [
#                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
#                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
#            ],
#            'layout': {
#                'title': 'Dash Data Visualization'
#            }
#        }
#    )

##############################################################
##################
############################################################## 
    html.Div([
        html.H5(children='Select part - 1', style={
                'width': '100%',
                'margin-left': 'auto',
                'margin-right': 'auto',
                'borderBottom': 'thin lightgrey solid',
                'float': 'center'}),
        html.Div([
                html.H5(children='Part type', style={
                        'width': '70%',
                        'float': 'center'}),
                dcc.Dropdown(
                    id='part-1-select',
                   # options=[{'label': i, 'value': i} for i in CPUIntel['name']],
                   options=[
                           {'label': 'Processor', 'value': 'Processor'},
                           {'label': 'GPU', 'value': 'GPU'},
                           {'label': 'Hard Drive', 'value': 'Hard Drive'},
                           {'label': 'RAM', 'value': 'RAM'},
                           ],
                    value='Fertility rate, total (births per woman)'
                ),
            ],
            style={'width': '20%', 'float': 'left', 'display': 'inline-block'}),
        html.Div([
                html.H5(children='Brand', style={
                                    'width': '50%',
                                    'float': 'center'}),
                dcc.Dropdown(
                    id='Processor-brand-select',
                   # options=[{'label': i, 'value': i} for i in CPUIntel['name']],
                   options=[
                           {'label': 'Intel', 'value': 'Intel'},
                           {'label': 'AMD', 'value': 'AMD'},
                           ],
                    value='Fertility rate, total (births per woman)'
                ),
            ],
            style={'width': '20%', 'float': 'center', 'margin-left': '70px', 'margin-right': '5px','display': 'inline-block'}),
    
            html.Div([
                    html.H5(children='Part Name', style={
                    'width': '70%',
                    'float': 'center'}),
                dcc.Dropdown(
                    id='Processor-model-select',
                    options=[{'label': i, 'value': i} for i in CPUIntel['name']],
                    value='Life expectancy at birth, total (years)'
                ),
            ], style={'width': '50%', 'float': 'right', 'display': 'inline-block'})
        ], style={
            'width': '60%',
             'margin-left': 'auto',
             'margin-right': 'auto',
            #'borderBottom': 'thin lightgrey solid',
            #'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }),

])


###############################################################
###################
###############################################################
#    html.H5(children='GPU', style={
#            'width': '40%',
#            'margin-left': 'auto',
#            'margin-right': 'auto',
#            'borderBottom': 'thin lightgrey solid',
#            'float': 'center'}),
################
#    html.Div([
#
#        html.Div([
#                html.H5(children='Brand', style={
#                                    'width': '50%',
#                                    'float': 'center'}),
#                dcc.Dropdown(
#                    id='GPU-brand-select',
#                   # options=[{'label': i, 'value': i} for i in CPUIntel['name']],
#                   options=[
#                           {'label': 'Nvidia', 'value': 'Nvidida'},
#                           {'label': 'AMD', 'value': 'AMD'},
#                           ],
#                    value='Fertility rate, total (births per woman)'
#                ),
#            ],
#            style={'width': '40%', 'float': 'center', 'display': 'inline-block'}),
#    
#            html.Div([
#                    html.H5(children='Part Name', style={
#                    'width': '55%',
#                    'float': 'center'}),
#                dcc.Dropdown(
#                    id='GPU-part-select',
#                    options=[{'label': i, 'value': i} for i in GPU['Name']],
#                    value='Life expectancy at birth, total (years)'
#                ),
#            ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'})
#        ], style={
#            'width': '40%',
#             'margin-left': 'auto',
#             'margin-right': 'auto',
#            #'borderBottom': 'thin lightgrey solid',
#            #'backgroundColor': 'rgb(256, 256, 256)',
#            'padding': '10px 5px'
#        }),
###############################################################
###################
###############################################################
#    html.H5(children='Hard Drive', style={
#            'width': '40%',
#            'margin-left': 'auto',
#            'margin-right': 'auto',
#            'borderBottom': 'thin lightgrey solid',
#            'float': 'center'}),
#    html.Div([
#        html.Div([
#                html.H5(children='Brand', style={
#                                    'width': '50%',
#                                    'float': 'center'}),
#                dcc.Dropdown(
#                    id='HDD-brand-select',
#                   # options=[{'label': i, 'value': i} for i in CPUIntel['name']],
#                   options=[
#                           {'label': 'Samsung', 'value': 'Samsung'},
#                           {'label': 'Crosair', 'value': 'Crosair'},
#                           ],
#                    value='Fertility rate, total (births per woman)'
#                ),
#            ],
#            style={'width': '40%', 'float': 'center', 'display': 'inline-block'}),
#    
#            html.Div([
#                    html.H5(children='Part Name', style={
#                    'width': '55%',
#                    'float': 'center'}),
#                dcc.Dropdown(
#                    id='HDD-part-select',
#                    options=[{'label': i, 'value': i} for i in HDDSDD['name']],
#                    value='Life expectancy at birth, total (years)'
#                ),
#            ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'})
#        ], style={
#            'width': '40%',
#             'margin-left': 'auto',
#             'margin-right': 'auto',
#            #'borderBottom': 'thin lightgrey solid',
#            #'backgroundColor': 'rgb(250, 250, 250)',
#            'padding': '10px 5px'
#        }),
#
###############################################################
###################
###############################################################
#    html.H5(children='RAM', style={
#                'width': '40%',
#                'margin-left': 'auto',
#                'margin-right': 'auto',
#                'borderBottom': 'thin lightgrey solid',
#                #'backgroundColor': 'rgb(250, 250, 250)',
#                'float': 'center'}),
#    html.Div([
#
#        html.Div([
#                html.H5(children='Brand', style={
#                                    'width': '50%',
#                                    'float': 'center'}),
#                dcc.Dropdown(
#                    id='RAM-brand-select',
#                   # options=[{'label': i, 'value': i} for i in CPUIntel['name']],
#                   options=[
#                           {'label': 'Samsung', 'value': 'Samsung'},
#                           {'label': 'Crosair', 'value': 'Crosair'},
#                           ],
#                    value='Fertility rate, total (births per woman)'
#                ),
#            ],
#            style={'width': '40%', 'float': 'center', 'display': 'inline-block'}),
#    
#            html.Div([
#                    html.H5(children='Part Name', style={
#                    'width': '55%',
#                    'float': 'center'}),
#                dcc.Dropdown(
#                    id='RAM-part-select',
#                    options=[{'label': i, 'value': i} for i in pdDDR4['name']],
#                    value='Life expectancy at birth, total (years)'
#                ),
#            ], style={'width': '55%', 'float': 'right', 'display': 'inline-block'})
#        ], style={
#            'width': '40%',
#             'margin-left': 'auto',
#             'margin-right': 'auto',
#            #'borderBottom': 'thin lightgrey solid',
#            'backgroundColor': 'rgb(256, 256, 256)',
#            'padding': '10px 5px'
#        }),
#    ])



if __name__ == '__main__':
    app.run_server(debug=True)