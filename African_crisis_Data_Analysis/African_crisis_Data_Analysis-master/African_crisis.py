# -*- coding: utf-8 -*-
"""
Analysis of African_crisis
Created on Thu Mar 19 11:44:04 2020

@author: Puruboi

"""
import pandas as pd   # import the lib panda as pd 
pd.__version__    # version of pandas 
dir(pd)    # gives the list of function in pd for acessing and manipulation 

# take a csv(excel file) path
path =r"C:\Users\Anonymous\Desktop\DataSet\african_crises.csv"
# read it into  the df
df2=pd.read_csv(path)
dir(pd.DataFrame())
# to get familarize with dataframes
df2.info()                    # info abt the frame compeletely
df2['case'].value_counts()    # no of times each values repeated in that coloumn
df2.columns                   # no of columns present
len(df2)                      # maximum rows 
df2.describe()                # gievs description like count, mean , std,etccc  expect for string( will not give for strings)
df2.describe(include='all')   # same as above but wil also give for strings too
df2.head()                    # first 5 rows
df2.tail()                    # last 5 rows
df2.head(10)                  # first 10 rows
df2.tail(10)                  # last 10 rows
df2.sample(10)                # gives random 10 samples 

df2['country'].value_counts()       # list all countries with their value counts (how many times its present)
len(df2['country'].value_counts())     # gives how many countries are there 
df2['year']
df2['year'].value_counts()
len(df2['year'].value_counts())
df2['year'].describe()                # gives the description 

df2['inflation_annual_cpi'][df2['country']=='Algeria'].min()
df2['inflation_annual_cpi'].max()
df2[['country','year']][df2['inflation_annual_cpi']==21989695.22]

df2['exch_usd']
df2['exch_usd'].value_counts()
df2['exch_usd'].describe()
df2['exch_usd'][df2['country']=='Algeria'].min()
df2['exch_usd'].max()
df2[['country','year']][df2['exch_usd']==744.3061387]
 
sum(df2['exch_usd'])

# converting to category datatype
df2.cc3=df2.cc3.astype('category')
df2.country=df2.country.astype('category')
df2.cc3.value_counts()
df2.country.value_counts()
df2.systemic_crisis =df2.systemic_crisis.astype('category')
df2.inflation_annual_cpi  =df2.inflation_annual_cpi .astype('category')
df2.inflation_crises
df2.year  =df2.year .astype('category')

df2['country'].apply(len)
df2['country'].apply(str.lower)

a=list(df2.groupby('country'))
df2.groupby('country').min()['independence']
df2.groupby('country').count()['independence']
df2.groupby('country').mean()['independence']
df2.groupby('country','systemic_crisis').agg(['mean','min','max','count','sum'])


# iloc
df = df2
df.iloc[2]
df.iloc[0]
df.iloc[0,2]
df.iloc[[3,4],[2,5]]
df.iloc[[range(3,10)],[2,5]] # this has to be done in list  ( give error )
df.iloc[list(range(3,10)),[2,5]] # like this ( solution)
df.iloc[list(range(3,10)),list(range(4,7))]

# loc
df.loc[0]
df.loc[0,'currency_crises']
df.loc[0,['country','year']]
df.loc[list(range(5)),['country','year']]

# .ix is deprecated. Please use
# .loc for label based indexing or
# .iloc for positional indexing'''
# indicating to import future 
# this helps to exceute py2.7 lines in py3.7 and viceversa 
# ix

df.ix[0]
df.ix[0,'country']
df.ix[0,3]
df.ix[0,2]

