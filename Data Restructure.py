# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 16:34:46 2017

@author: Shawn Z
"""

import pandas as pd
import numpy as np

#---------------Import Features----------------------
CR=pd.read_csv('current_fixed.csv').values.flatten()
#Imp_Vol_3M=pd.read_csv('3MO_PUT_IMP_VOL_fixed.csv').values.flatten()
#Imp_Vol_10D=pd.read_csv('PUT_IMP_VAL_10D_fixed.csv').values.flatten()
Imp_Vol_Delta=pd.read_csv('NYSE Delta_vol_fixed.csv').values.flatten()
Asset_Turnover_fixed=pd.read_csv('Asset_Turnover_fixed.csv').values.flatten()
D2A=pd.read_csv('D2A.csv').values.flatten()
PE_fixed=pd.read_csv('PE_fixed.csv').values.flatten()
PX_close=pd.read_csv('PX_close_fixed.csv').values.flatten()
Vol_X=pd.read_csv('Total_Volatility_fixed.csv').values.flatten()
Inv_Cap=pd.read_csv('Total_Invested_Capital_fixed.csv').values.flatten()

NYSE_Tr=pd.read_csv('NYSE Google Trend_fixed.csv').values.flatten(1)
VIX_Tr=pd.read_csv('VIX Google Trend_fixed.csv').values.flatten(1)

#----------------Import Y-----------------------------
Vol_Y=pd.read_csv('NYSE VOLATILITY_90D_Y_fixed.csv').values.flatten()
Y=Vol_Y

#----------------Build X---------------------------
X=pd.DataFrame()
X['CR']=CR
#X['Imp_Vol_3M']=Imp_Vol_3M
#X['Imp_Vol_10D']=Imp_Vol_10D
X['Imp_Vol_Delta']=Imp_Vol_Delta
X['Asset_Turnover_fixed']=Asset_Turnover_fixed
X['D2A']=D2A
X['NYSE_Tr']=NYSE_Tr
X['PE']=PE_fixed
X['PX_close']=PX_close
X['Vol_X']=Vol_X
X['VIX_Tr']=VIX_Tr
X['Inv_Cap']=Inv_Cap

#-----------------Build Y------------------
X['Y']=Y
X=X.dropna() # drop nan in X or Y
Y=X['Y']
X=X[X.columns[:-1]]


