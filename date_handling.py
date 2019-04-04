#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:27:21 2019

@author: thatchernew
"""

# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import inspect


from statsmodels.stats.anova import anova_lm

from datetime import timedelta, date


#### DATETIME OPERATIONS ####

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def datespan(start_date, num_days):
    for n in range(0, num_days):
        yield start_date + timedelta(n)



start_date = date(2015, 1, 1)
#end_date = date(2015, 6, 2)
#print(str(dateprior(start_date)))
#print(dateprior(end_date))


#### INTAKE AND PROFILE DATA ####

df = pd.read_csv('/Users/thatchernew/BC_Stuff/Digico/BTCDigico.csv')
#print(' + '.join(df.columns))

#process data (add a time series column, index on that column)
df['datetime'] = pd.to_datetime(df['Date'])
df = df.set_index('datetime')
df.drop(['Date'], axis=1, inplace=True)

#print(df.dtypes)
'''
AdrActSentCnt       int64
AdrBalAdjCnt        int64
CapRealUSD          int64
IssContPctAnn     float64
NVTAdj90          float64
PriceUSD          float64
RevAllTimeUSD       int64
SplyAct1yr        float64
TxTfrValAdjUSD    float64
UTXOCnt             int64
VelActAdj1yr      float64
'''

'''
for col in df.columns:
    print('{}, {}'.format(df[col].name, df[col].dtype))
    print(df[col].head(1))
'''

#### PERFORM OPERATIONS ON A LIST OF COLUMNS
    
#Take price from next day
next_day_dependant = 'PriceUSD'

#Input list of desired predictor variables
predictor_list = ['AdrActSentCnt', 'AdrBalAdjCnt' 'CapRealUSD' 'IssContPctAnn']

#Input date and length of time to run regressions for (days, currently)
single_date = date(2017, 1, 2)
regression_span = 7

#print(df.loc[single_date])
#print(df.loc[df['PriceUSD'] > 900])


'''
try:
    next_price = df.loc[str(dateafter(single_date)), ['PriceUSD']]
    print(next_price[0])
except KeyError as err:
    print('KeyError: {0}'.format(err))
'''


def safe_run(func):
    def func_wrapper(*args, **kwargs):
        try:
           return func(*args, **kwargs)
        except Exception as e:
            #print(e)
            return e
    return func_wrapper

@safe_run
def dateafter(start_date):
    r = start_date + timedelta(1)
    return r

@safe_run
def dateprior(start_date):
    r = start_date + timedelta(x)
    return r


f = dateprior(date(2017,1,1))
#print(f.__dir__())
#print(f.args)
#print(f.with_traceback())
#print(f)
print(type(f).__name__)
print(f.args)
print(f)


