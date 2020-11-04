# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:56:20 2020
@author: Anonymous
"""
# importing libraries
#%matplotlib inline
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('Modules are imported')

# importing covid-19 Dataset
path = r"C:\Users\Anonymous\Desktop\Puruboi\Towards_Data_science\COVID19 Data Analysis Using Python\covid19_Confirmed_dataset.csv"
df = covid_dataset_csv = pd.read_csv(path)
df.head(10)

# check the shape of dataframe
a = df.shape
print("shape of dataframe covid_dataset_csv in format(rows,columns): ",a)

#delete the useless columns

# df_drp= df.drop(["Lat","Long"],axis=1) # axis = 0 means rows and axis = 1 col , default axis wil be 0
# returns copy of dataset after drop specified particulars

df.drop(["Lat","Long"],axis=1,inplace=True)
# above line will instantly drop the particulars from dataset itself 

# Aggregating the rows by the country 
df_aggregated = df.groupby("Country/Region").sum() # now the index will be countries for this dataset
df_aggregated.head(10)
df_aggregated.shape

# visualising Data related to a country for example india 

df_aggregated.loc["India"].plot()
df_aggregated.loc["US"].plot()
df_aggregated.loc["Italy"].plot()
df_aggregated.loc["Spain"].plot()
plt.legend()

# calculating good measure 

df_aggregated.loc["China"][:3].plot()

# to find rate of the curve , first we find 1st derivative 

df_aggregated.loc["China"].diff().plot() # shows the change in infection rate day by day 

# find maximum infection rate for these countries with respect to countries
a = df_aggregated.loc["India"].diff().max()
b = df_aggregated.loc["US"].diff().max()
c = df_aggregated.loc["Italy"].diff().max()
d = df_aggregated.loc["Spain"].diff().max()
e = df_aggregated.loc["China"].diff().max()
print("The max infection rate of each country, india = {}, Us = {}, Italy= {}, Spain = {}, China = {}.".format(a,b,c,d,e))

# to calculate max infection rate of all countries
countries = list(df_aggregated.index)
max_infection_rates = []
for c in countries :
    max_infection_rates.append(df_aggregated.loc[c].diff().max())
df_aggregated["max_infection_rates"] = max_infection_rates

# created a new dataset with only needed columns

df_aggregated_new = pd.DataFrame(df_aggregated["max_infection_rates"])
df_aggregated_new.head()
#df_aggregated_new.plot()


# importing the world happiness report.csv file

path_2 = r"C:\Users\Anonymous\Desktop\Puruboi\Towards_Data_science\COVID19 Data Analysis Using Python\worldwide_happiness_report.csv"
happiness_report = pd.read_csv(path_2)
happiness_report.head(10)

useless_col = ["Ladder score", "Generosity", "Perceptions of corruption"]
happiness_report.drop(useless_col,axis = 1,inplace = True)
happiness_report.head(10)

#changing indicies of DataFrame()

happiness_report.set_index("Country name",inplace = True)
happiness_report.head()

# Now join the both datasets df_aggregated_new,happiness_report
# covid_19 dataset
df_aggregated_new
df_aggregated_new.shape

#happiness_report
happiness_report
happiness_report.shape

# linear join 
data = df_aggregated_new.join(happiness_report,how = "inner")
data.head()

# checking the correlation (correlation Matrix)

data.corr()  # if the calue btw both is higer then the correlation is higher
data.to_excel("./Correlation_check.xlsx")  # loading to Excel

# visualising the results using seaborn module

#Plotting  GDP vs Max_infection_rate 
x = data["Logged GDP per capita"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#Healthy life expectancy vs max_infection_rates
x = data["Healthy life expectancy"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#Social support vs max_infection_rates
x = data["Social support"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#Freedom to make life choices vs max_infection_rates
x = data["Freedom to make life choices"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#lowerwhisker vs max_infection_rates
x = data["lowerwhisker"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#upperwhisker vs max_infection_rates
x = data["upperwhisker"]
y = data["max_infection_rates"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))