# -*- coding: utf-8 -*-
"""
Created on 10/29/2019
Modified on 11/11/2021

@author: Concetta D'Amato
@license: creative commons 4.0
"""


import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import matplotlib.dates as mdates
import plotly.express as px
import plotly.graph_objects as go
from matplotlib import rc
import matplotlib.style as style 
import xarray as xr
import datetime
from IPython.display import Image

##############################################################################################################################INTRODUZIONE####
def show_var(variabile):
    df = pd.read_csv(variabile+'_1.csv',skiprows=6, sep=',', parse_dates=[0], na_values=-9999,usecols=[1,2])
    df.columns = ['Datetime',variabile]

    fig = px.line(df, x='Datetime', y=variabile)
    if variabile=='airT':
        fig.update_yaxes(title_text='Temperature [°C]')
    if variabile=='Wind':
        fig.update_yaxes(title_text='Velocità vento [m/s] ')
    if variabile=='GHF':
        fig.update_yaxes(title_text='Flussio di calore dal suolo')
    if variabile=='Pres':
        fig.update_yaxes(title_text='Pressione')
    if variabile=='SoilMoisture_sin':
        fig.update_yaxes(title_text='Contenuto di acqua')
    if variabile=='LAI':
        fig.update_yaxes(title_text='LAI')
    if variabile=='RH':
        fig.update_yaxes(title_text='Umidità relativa')
    if variabile=='ShortwaveDirect':
        fig.update_layout(title='Short wave direct')
        fig.update_yaxes(title_text='Radiazione corta diretta [$W \cdot m^{−2}$]')
    if variabile=='ShortwaveDiffuse':
        fig.update_layout(title='Short wave diffuse')
        fig.update_yaxes(title_text='Radiazione corta diffusa [$W \cdot m^{−2}$]')
    if variabile=='LongDownwelling':
        fig.update_layout(title='Long wave')
        fig.update_yaxes(title_text='Radiazione lunga incidente [$W \cdot m^{−2}$]')
    if variabile=='Net':
        fig.update_layout(title='Net radiation')
        fig.update_yaxes(title_text='Radiazione netta [$W \cdot m^{−2}$]')
    
    #fig.update_xaxes(rangeslider_visible=True)
    fig.show()

    
##############################################################################################################################
##############################################################################################################################    PROSPERO   ####
##############################################################################################################################
def show_stress(a,b,c,d):
    warnings.filterwarnings('ignore')
    kl = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kl = kl.drop(['Format'],axis=1) 
    kl.columns.values[0] = 'Date'
    kl.columns.values[1] = 'Potential'  
    kl.Potential[kl.Potential<0]=0
      
    kl3 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kl3 = kl3.drop(['Format'],axis=1)
    kl3.columns.values[0] = 'Date'
    kl3.columns.values[1] = 'Environmental_Stress'
    kl3.Environmental_Stress[kl3.Environmental_Stress<0]=0
        
    kl2 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kl2 = kl2.drop(['Format'],axis=1)
    kl2.columns.values[0] = 'Date'
    kl2.columns.values[1] = 'Water_Stress'
    kl2.Water_Stress[kl2.Water_Stress<0]=0
    
    kl4 = pd.read_csv(d,skiprows=6,parse_dates=[1])
    kl4 = kl4.drop(['Format'],axis=1)
    kl4.columns.values[0] = 'Date'
    kl4.columns.values[1] = 'Total_Stress'
    kl4.Total_Stress[kl4.Total_Stress<0]=0
    
    
   
    fig = px.line()
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl['Potential'], mode='lines', name='Potential'))
    fig.add_trace(go.Scatter(x=kl3['Date'], y=kl3['Environmental_Stress'], mode='lines', name='Environmental_Stress'))
    fig.add_trace(go.Scatter(x=kl2['Date'], y=kl2['Water_Stress'], mode='lines', name='Water_Stress'))
    fig.add_trace(go.Scatter(x=kl4['Date'], y=kl4['Total_Stress'], mode='lines', name='Total_Stress'))
    

    #fig.update_xaxes(rangeslider_visible=True)
    
    fig.update_layout(
        title= "Traspirazione in funzione dei vari fattori di stress",
        xaxis_title="Data",
        yaxis_title= "Traspirazione [mm]",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        legend_title="Tipologia di Stress",
        font=dict(size=14))
    
    fig.show()
###### GRAFICO TEMPERATURA FOGLIA AL SOLE ########
def show_T_S(a,b,c,d):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kT = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kT = kT.drop(['Format'],axis=1)
    kT.columns.values[0] = 'Date'
    kT.columns.values[1] = 'Tpotenziale'
    #kT.EvapoTranspiration[kl.EvapoTranspiration<0]=0
   
    
    kT2 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kT2 = kT2.drop(['Format'],axis=1)
    kT2.columns.values[0] = 'Date'
    kT2.columns.values[1] = 'Tstress_ambientali'
    #kT2.Evaporation[kl2.Evaporation<0]=0
  
    
    kT3 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kT3 = kT3.drop(['Format'],axis=1)
    kT3.columns.values[0] = 'Date'
    kT3.columns.values[1] = 'Tstress_acqua'
    #kT3.Transpiration[kl3.Transpiration<0]=0
    
    
    kT4 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kT4 = kT4.drop(['Format'],axis=1)
    kT4.columns.values[0] = 'Date'
    kT4.columns.values[1] = 'Tstress_totali'
    #kT4.Transpiration[kl3.Transpiration<0]=0
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kT['Date'], y=kT['Tpotenziale'], mode='lines', name='Tpotenziale'))
    fig.add_trace(go.Scatter(x=kT2['Date'], y=kT2['Tstress_ambientali'], mode='lines', name='Tstress_ambientali'))
    fig.add_trace(go.Scatter(x=kT3['Date'], y=kT3['Tstress_acqua'], mode='lines', name='Tstress_acqua'))
    fig.add_trace(go.Scatter(x=kT4['Date'], y=kT4['Tstress_totali'], mode='lines', name='Tstress_totali'))
    
    fig.update_layout(
        title= "Temperatura delle foglie esposte al sole in funzione dei vari stress",
        xaxis_title="Data",
        yaxis_title= "Temperatura [K]",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        legend_title="Tipologia di Stress",
        font=dict(size=14))
    fig.show()
###### GRAFICO CONFROLTO DEI LAI ########
def confrontoET_lai(a,b):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kETC = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kETC = kETC.drop(['Format'],axis=1)
    kETC.columns.values[0] = 'Date'
    kETC.columns.values[1] = 'Evapotraspirazione_cost'
    #kT.EvapoTranspiration[kl.EvapoTranspiration<0]=0
   
    
    kETS = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kETS = kETS.drop(['Format'],axis=1)
    kETS.columns.values[0] = 'Date'
    kETS.columns.values[1] = 'Evapotraspirazione_sin'
    #kT2.Evaporation[kl2.Evaporation<0]=0
  

    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kETC['Date'], y=kETC['Evapotraspirazione_cost'], mode='lines', name='ET LAI = 1', line_color = "salmon"))
    fig.add_trace(go.Scatter(x=kETS['Date'], y=kETS['Evapotraspirazione_sin'], mode='lines', name='ET LAI = sin', line_color = "silver"))
    
    
    fig.update_layout(
        title= "Confronto evapotraspirazione con LAI = 1 e LAI = sin ",
        xaxis_title="Data",
        yaxis_title= "Evapotraspirazione [mm/h]",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        legend_title="Tipologia di LAI",
        font=dict(size=14))
    fig.show()
    
    
 ###### GRAFICO CONFROLTO stress ########
def confrontoET_stress(a,b,c,d):
    warnings.filterwarnings('ignore')
 ############################ GRAFICO 1 ########################################
    kETP = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kETP = kETP.drop(['Format'],axis=1)
    kETP.columns.values[0] = 'Date'
    kETP.columns.values[1] = 'ETpotenziale'
    #kT.EvapoTranspiration[kl.EvapoTranspiration<0]=0
   
    
    kETE = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kETE = kETE.drop(['Format'],axis=1)
    kETE.columns.values[0] = 'Date'
    kETE.columns.values[1] = 'ETstress_ambientali'
    #kT2.Evaporation[kl2.Evaporation<0]=0
  
    
    kETW = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kETW = kETW.drop(['Format'],axis=1)
    kETW.columns.values[0] = 'Date'
    kETW.columns.values[1] = 'ETstress_acqua'
    #kT3.Transpiration[kl3.Transpiration<0]=0
    
    
    kETT = pd.read_csv(d,skiprows=6,parse_dates=[1])
    kETT = kETT.drop(['Format'],axis=1)
    kETT.columns.values[0] = 'Date'
    kETT.columns.values[1] = 'ETstress_totali'
    #kT4.Transpiration[kl3.Transpiration<0]=0
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kETP['Date'], y=kETP['ETpotenziale'], mode='lines', name='ETpotenziale', line_color = "orangered"))
    fig.add_trace(go.Scatter(x=kETE['Date'], y=kETE['ETstress_ambientali'], mode='lines', name='ETstress_ambientali', line_color = "greenyellow"))
    fig.add_trace(go.Scatter(x=kETW['Date'], y=kETW['ETstress_acqua'], mode='lines', name='ETstress_acqua', line_color = "turquoise" ))
    fig.add_trace(go.Scatter(x=kETT['Date'], y=kETT['ETstress_totali'], mode='lines', name='ETstress_totali', line_color = "fuchsia"))
    
    fig.update_layout(
        title= "Confronto delle varie tipologie di stress nell'evapotraspirazione",
        xaxis_title="Data",
        yaxis_title= "Evapotraspirazione [mm/h]",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        legend_title="Tipologia di Stress",
        font=dict(size=14))
    fig.show()    
    
 ###### GRAFICO CONFROLTO MODELLI ########
def confrontoET_modelli(a,b,c):
    warnings.filterwarnings('ignore')
 ############################ GRAFICO 1 ########################################
    kPM = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kPM = kPM.drop(['Format'],axis=1)
    kPM.columns.values[0] = 'Date'
    kPM.columns.values[1] = 'ET Penman-Monteith FAO'
    #kT.EvapoTranspiration[kl.EvapoTranspiration<0]=0
   
    
    kPT = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kPT = kPT.drop(['Format'],axis=1)
    kPT.columns.values[0] = 'Date'
    kPT.columns.values[1] = 'ET Priestley-Taylor'
    #kT2.Evaporation[kl2.Evaporation<0]=0
  
    
    kPR = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kPR = kPR.drop(['Format'],axis=1)
    kPR.columns.values[0] = 'Date'
    kPR.columns.values[1] = 'ET Prospero'
    #kT3.Transpiration[kl3.Transpiration<0]=0
    
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kPT['Date'], y=kPT['ET Priestley-Taylor'], mode='lines', name='ET Priestley-Taylor', line_color = "dodgerblue"))
    fig.add_trace(go.Scatter(x=kPM['Date'], y=kPM['ET Penman-Monteith FAO'], mode='lines', name='ET Penman-Monteith FAO', line_color = "goldenrod"))
    fig.add_trace(go.Scatter(x=kPR['Date'], y=kPR['ET Prospero'], mode='lines', name='ET Prospero', line_color = "hotpink" ))
     
    fig.update_layout(
        title= "Confronto delle varie tipologie di modelli di evapotraspirazione",
        xaxis_title="Data",
        yaxis_title= "Evapotraspirazione [mm/h]",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        legend_title="Tipologia di modelli",
        font=dict(size=14))
    fig.show()     
    
    
    
########TEMPERATURA FOGLIE OMBRA############### 
def show_T_O(a,b,c,d):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kTO = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kTO = kTO.drop(['Format'],axis=1)
    kTO.columns.values[0] = 'Date'
    kTO.columns.values[1] = 'Tpotenziale'
    #kT.EvapoTranspiration[kl.EvapoTranspiration<0]=0
   
    
    kTO2 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kTO2 = kTO2.drop(['Format'],axis=1)
    kTO2.columns.values[0] = 'Date'
    kTO2.columns.values[1] = 'Tstress_ambientali'
    #kT2.Evaporation[kl2.Evaporation<0]=0
  
    
    kTO3 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kTO3 = kTO3.drop(['Format'],axis=1)
    kTO3.columns.values[0] = 'Date'
    kTO3.columns.values[1] = 'Tstress_acqua'
    #kT3.Transpiration[kl3.Transpiration<0]=0
    
    
    kTO4 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kTO4 = kTO4.drop(['Format'],axis=1)
    kTO4.columns.values[0] = 'Date'
    kTO4.columns.values[1] = 'Tstress_totali'
    #kT4.Transpiration[kl3.Transpiration<0]=0
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kTO['Date'], y=kTO['Tpotenziale'], mode='lines', name='Tpotenziale'))
    fig.add_trace(go.Scatter(x=kTO2['Date'], y=kTO2['Tstress_ambientali'], mode='lines', name='Tstress_ambientali'))
    fig.add_trace(go.Scatter(x=kTO3['Date'], y=kTO3['Tstress_acqua'], mode='lines', name='Tstress_acqua'))
    fig.add_trace(go.Scatter(x=kTO4['Date'], y=kTO4['Tstress_totali'], mode='lines', name='Tstress_totali'))
    
    fig.update_layout(
        title= "Temperatura delle foglie in ombra in funzione dei vari stress",
        xaxis_title="Data",
        yaxis_title= "Temperatura [K]",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        legend_title="Tipologia di Stress",
        font=dict(size=14))
    fig.show()

def show_E_T(a,b,c):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kl = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kl = kl.drop(['Format'],axis=1)
    kl.columns.values[0] = 'Data'
    kl.columns.values[1] = 'Evapotraspirazione'
    #kl.EvapoTranspiration[kl.EvapoTranspiration<0]=0
   
    
    kl2 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kl2 = kl2.drop(['Format'],axis=1)
    kl2.columns.values[0] = 'Data'
    kl2.columns.values[1] = 'Evaporazione'
    #kl2.Evaporation[kl2.Evaporation<0]=0
  
    
    kl3 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kl3 = kl3.drop(['Format'],axis=1)
    kl3.columns.values[0] = 'Data'
    kl3.columns.values[1] = 'Traspirazione'
    #kl3.Transpiration[kl3.Transpiration<0]=0
    
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kl['Data'], y=kl['Evapotraspirazione'], mode='lines', name='Evapotraspirazione'))
    fig.add_trace(go.Scatter(x=kl['Data'], y=kl2['Evaporazione'], mode='lines', name='Evaporazione'))
    fig.add_trace(go.Scatter(x=kl['Data'], y=kl3['Traspirazione'], mode='lines', name='Traspirazione'))

   #fig.update_xaxes(rangeslider_visible=True)
    
    
    fig.update_layout(
        title= "Contributo di evaporazione e traspirazione nell'evapotraspirazione",
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        xaxis_title="Data",
        yaxis_title="[mm/h]",
        legend_title="Contributi all'ET",
        font=dict(size=14))
    fig.show()
    
def show_compare_EvapoTranspiration(a,b,c):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kl = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kl = kl.drop(['Format'],axis=1)
    kl.columns.values[0] = 'Date'
    kl.columns.values[1] = 'Prospero_ET'
    kl.Prospero_ET[kl.Prospero_ET<0]=0
  
    kl2 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kl2 = kl2.drop(['Format'],axis=1)
    kl2.columns.values[0] = 'Date'
    kl2.columns.values[1] = 'Pristley_Taylor_ET'
    kl2.Pristley_Taylor_ET[kl2.Pristley_Taylor_ET<0]=0
  
    kl3 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kl3 = kl3.drop(['Format'],axis=1)
    kl3.columns.values[0] = 'Date'
    kl3.columns.values[1] = 'PenmanMontheithFAO_ET'
    kl3.PenmanMontheithFAO_ET[kl3.PenmanMontheithFAO_ET<0]=0
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl['Prospero_ET'], mode='lines', name='Prospero_ET'))
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl2['Pristley_Taylor_ET'], mode='lines', name='Pristley_Taylor_ET'))
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl3['PenmanMontheithFAO_ET'], mode='lines', name='PenmanMontheithFAO_ET'))

   #fig.update_xaxes(rangeslider_visible=True)
    
    
    fig.update_layout(
        title='Compare EvapoTraspiration fluxes',
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        #xaxis_title="Date",
        yaxis_title="[$W\cdot m^{−2}$]",
        #legend_title="Date",
        font=dict(size=14))
    fig.show()


def compare_sim_obs(a,b):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kl = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kl = kl.drop(['Format'],axis=1)
    kl.columns.values[0] = 'Date'
    kl.columns.values[1] = 'GEO-SPACE'
    kl.LysGEO[kl.LysGEO<0]=0
   
    
    kl2 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kl2 = kl2.drop(['Format'],axis=1)
    kl2.columns.values[0] = 'Date'
    kl2.columns.values[1] = 'obs'
    kl2.SpikeII_data[kl2.SpikeII_data<0]=0
    
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl['GEO-SPACE'], mode='lines', name='GEO-SPACE'))
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl2['obs'], mode='lines', name='obs'))

   #fig.update_xaxes(rangeslider_visible=True)
    
    
    fig.update_layout(
        title='Compare GEO-SPACE and observation data',
        #xaxis_title="Date"
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        yaxis_title="$Evapotranspiration -[mm h^{-1}]$",
        #legend_title="Date",
        font=dict(size=18))
    fig.show()
    
    
def compare3(a,b,c):
    warnings.filterwarnings('ignore')
    ############################ GRAFICO 1 ########################################
    kl = pd.read_csv(a,skiprows=6,parse_dates=[1])
    kl = kl.drop(['Format'],axis=1)
    kl.columns.values[0] = 'Date'
    kl.columns.values[1] = 'GEOSPACE'
    kl.GEOSPACE[kl.GEOSPACE<0]=0
    
    kl2 = pd.read_csv(b,skiprows=6,parse_dates=[1])
    kl2 = kl2.drop(['Format'],axis=1)
    kl2.columns.values[0] = 'Date'
    kl2.columns.values[1] = 'Dataset_1'
    kl2.Dataset_1[kl2.Dataset_1<0]=0
    
    kl3 = pd.read_csv(c,skiprows=6,parse_dates=[1])
    kl3 = kl3.drop(['Format'],axis=1)
    kl3.columns.values[0] = 'Date'
    kl3.columns.values[1] = 'Dataset_2'
    kl3.Dataset_2[kl3.Dataset_2<0]=0
    
    
    fig = px.line()
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl['GEO-SPACE'], mode='lines', name='GEO-SPACE'))
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl2['Dataset_1'], mode='lines', name='Dataset_1'))
    fig.add_trace(go.Scatter(x=kl['Date'], y=kl3['Dataset_2'], mode='lines', name='Dataset_2'))
    
    fig.update_layout(
        title='Compare GEO-SPACE and two observation dataset',
        #xaxis_title="Date"
        font_family="Times New Roman",
        font_color="Black",
        title_font_family="Times New Roman",
        title_font_color="Black",
        #yaxis_title="$Evapotranspiration -[mm h^{-1}]$",
        #legend_title="Date",
        font=dict(size=18))
    fig.show()