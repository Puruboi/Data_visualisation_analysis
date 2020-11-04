# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:57:17 2020

@author: Anonymous
""" 
"""Getting data from Worldometers.info JHU"""
    
from covid import Covid
import pandas as pd
#Get All Data

covid = Covid()
c=covid.get_data()
df = pd.DataFrame(c)
df.to_excel("./Corona_details_JNU.xlsx");

#Getting data from Worldometers.info worldometers

covid = Covid(source="worldometers")
d= covid.get_data()
df = pd.DataFrame(c)
df.to_excel("./Corona_details_worldmeters.xlsx");

"""
#List Countries
countries = covid.list_countries()
print('The list of the countries: ',countries)

#send data to dataframe and loading into excel

#Get Status By Country ID
cases_1 = covid.get_status_by_country_id(115)
print('the covid status of country with id-115: ',cases_1)

#Get Status By Country Name
country = str(input('enter the country name to knw the status: '))
cases = covid.get_status_by_country_name(country)
for x in cases:
    print(x,":",cases[x])
print('The total case status wrt to {} : {}'.format(country,cases)) 
   
#Get Total Active cases
active = covid.get_total_active_cases()  
print('the total active cases :  ',active)
#Get Total Confirmed cases

confirmed = covid.get_total_confirmed_cases()
print('the total confirmed cases :  ',confirmed)

#Get Total Recovered cases

recovered = covid.get_total_recovered()
print('the total recovered cases :  ',recovered)
#Get Total Deaths

deaths = covid.get_total_deaths()
print('the total death cases :  ',deaths)
"""
"""
#Getting data from Worldometers.info worldometers

covid = Covid(source="worldometers")

#Get Data

covid.get_data()

#List Countries
countries = covid.list_countries()
print('The list of the countries: ',countries)

#Get Status By Country ID
cases_1 = covid.get_status_by_country_id(115)
print('the covid status of country with id-115: ',cases_1)

#Get Status By Country Name
country = str(input('enter the country name to knw the status: '))
cases = covid.get_status_by_country_name(country)
for x in cases:
    print(x,":",cases[x])
print('The total case status wrt to {} : {}'.format(country,cases)) 
   
#Get Total Active cases
active = covid.get_total_active_cases()  
print('the total active cases :  ',active)
#Get Total Confirmed cases

confirmed = covid.get_total_confirmed_cases()
print('the total confirmed cases :  ',confirmed)

#Get Total Recovered cases

recovered = covid.get_total_recovered()
print('the total recovered cases :  ',recovered)
#Get Total Deaths

deaths = covid.get_total_deaths()
print('the total death cases :  ',deaths)
"""