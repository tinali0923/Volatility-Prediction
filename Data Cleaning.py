# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


def clean(sheetname):
    data=pd.read_excel('Data.xlsx', sheetname=sheetname)
    col=data.columns
    merge1=pd.DataFrame()
    merge1[col[0]]=data[col[0+1]][2:]
    merge1['Date']=data[col[0]][2:]
    merge1=merge1.set_index('Date')
    
    
    i=3
    length=len(col)
    while i < length:  
        merge2=pd.DataFrame()
        merge2[col[i]]=data[col[i+1]][2:]
        merge2['Date']=data[col[i]][2:]
        merge2=merge2.drop_duplicates(subset='Date', keep='first').set_index('Date')
        
        merge1=pd.concat([merge1,merge2], join_axes=[merge1.index],axis=1)
        #pd.concat([df1, df4], axis=1, join='inner')
        i+=3
    
    merge1.to_csv('NYSE '+sheetname+'.csv')
    
clean('VOLATILITY_90D')
clean('PE_RATIO')
clean('TOTAL_INVESTED_CAPITAL')
clean('ASSET_TURNOVER')
clean('CUR_RATIO')
clean('TOT_DEBT_TO_TOT_ASSET')
clean('PX_CLOSE_1D')
clean('PUT_IMP_VOL_10D')
clean('3MO_PUT_IMP_VOL')