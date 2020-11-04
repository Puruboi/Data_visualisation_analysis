# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:44:33 2020

@author: Puruboii
"""

from covid import Covid
import pandas as pd
#Get All Data

covid = Covid()
c=covid.get_data()
df = pd.DataFrame(c)
print("JNU corona details dataframe: ",df)
df.to_excel("./Corona_details_JNU.xlsx");

#Getting data from Worldometers.info worldometers

covid = Covid(source="worldometers")
d= covid.get_data()
df_1= pd.DataFrame(d)
print("JNU corona details dataframe: ",df_1)
df.to_excel("./Corona_details_worldmeters.xlsx");

#Get Status By Country Name
country = str(input('enter the country name to knw the status: '))
cases = covid.get_status_by_country_name(country)
for x in cases:
    print(x,":",cases[x])
print('The total case status wrt to {} : {}'.format(country,cases)) 