# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:28:03 2020

@author: Anonymous
"""
"""Analyze Box Office Data with Seaborn and Python
Now, you will apply various graphical techniques using Seaborn to analyze worldwide box office revenue. We will accomplish this with the help of following tasks in the project:

Data Loading and Exploration
Visualizing the Target Distribution
Comparing Film Revenue to Budget
Do Official Homepages Impact Revenue?
Distribution of Languages across Films
Common Words in Film Titles and Descriptions
How do Film Descriptions Impact Revenue?"""

# importing Libraries
import numpy as np
import pandas as pd
pd.set_option('max_columns', None)
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import datetime
from scipy import stats
from scipy.sparse import hstack, csr_matrix
from sklearn.model_selection import train_test_split, KFold
from wordcloud import WordCloud
from collections import Counter
from nltk.corpus import stopwords
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import StandardScaler
import nltk
nltk.download('stopwords')
stop = set(stopwords.words('english'))
import os
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import json
import ast
from urllib.request import urlopen
from PIL import Image
import eli5
from sklearn.linear_model import LinearRegression
print("Libraries Imported ")


#data loading and exploring
# Loading Data
path_1 = r"C:\Users\Anonymous\Desktop\Puruboi\Towards_Data_science\Box_office_Analyse_1\train (0).csv" # train set path
path_2 = r"C:\Users\Anonymous\Desktop\Puruboi\Towards_Data_science\Box_office_Analyse_1\test (0).csv" # test set path 
train = pd.read_csv(path_1)
test = pd.read_csv(path_2)
#Exploring Data
print(train.info())
print(train.describe())
print(test.info())
print(test.describe())
print(train.head())
print(train.shape)
print(test.head())
print(test.shape)

# visualising the data 
#train.revenue.hist()
# Subplot 
fig, ax=plt.subplots(figsize = (16,6))
plt.subplot(1,2,1)
sns.distplot(train['revenue'], kde=False)
plt.title('Distribution of revenue')
plt.subplot(1,2,2)
sns.distplot(np.log1p(train['revenue']), kde = False) #Normalising 
plt.title('Distribution of log-transformed revenue')

# adding normalised revenue to dataset
train['log_revenue'] = np.log1p(train['revenue'])


#Relationship btw film revenue and Budget

plt.figure(figsize=(16,8))
plt.subplot(1,2,1)
sns.scatterplot(train['budget'], train['revenue'])
plt.title('Revenue vs Budget')
plt.subplot(1,2,2)
sns.scatterplot(np.log1p(train['budget']), train['log_revenue'])
plt.title('Log Revenue vs Log Budget')

# nornalising and adding to dataset
train['log_budget'] = np.log1p(train['budget'])
test['log_budget'] = np.log1p(test['budget'])


# Does having an Official Homepage Affect Revenue?
train['homepage'].value_counts().head(10)

train['has_hompage'] = 0
train.loc[train['homepage'].isnull()==False, 'has_homepage'] = 1
test['has_hompage'] = 0
test.loc[test['homepage'].isnull()==False, 'has_homepage'] = 1

sns.catplot(x = 'has_hompage' , y= 'revenue', data=train);
plt.title('Revenue for films with and without a hompage');

# Distribution of Languages in Film 

language_data = train.loc[train['original_language'].isin(train['original_language'].value_counts().head(10).index)]

plt.figure(figsize=(16,8))
plt.subplot(1,2,1)
sns.boxplot(x = 'original_language', y = 'revenue', data = language_data)
plt.title('Mean revenue per language')
plt.subplot(1,2,2)
sns.boxplot(x = 'original_language', y = 'log_revenue', data=language_data)
plt.title('Mean log revenue per language')


# Frequent Words in Film Titles and Descriptions

plt.figure(figsize=(12, 12))
text = ' '.join(train['original_title'].values)
wordcloud = WordCloud(max_font_size = None,
                      background_color = 'white',
                      width=1200, height=1000).generate(text)
plt.imshow(wordcloud)
plt.title('Top words across movie titles')
plt.axis('off')
plt.show()

plt.figure(figsize=(12, 12))
text = ' '.join(train['overview'].fillna('').values)
wordcloud = WordCloud(max_font_size = None,
                      background_color = 'white',
                      width=1200, height=1000).generate(text)
plt.imshow(wordcloud)
plt.title('Top words across movie overviews')
plt.axis('off')
plt.show()

# Do Film Descriptions Impact Revenue?


vectorizer = TfidfVectorizer(
sublinear_tf = True,
analyzer = 'word',
token_pattern = r'\w{1,}',
ngram_range = (1,2),
min_df = 5)

overview_text = vectorizer.fit_transform(train['overview'].fillna(''))
linreg = LinearRegression()
linreg.fit(overview_text, train['log_revenue'])
eli5.show_weights(linreg, vec=vectorizer, top=20, feature_filter = lambda x : x != '<BIAS>')


# Analyse movie dates

test.loc[test['release_date'].isnull()==False, 'release_date'].head()

# preprocessing Feature 
# adding 20 for 21st century dates and 19 for 19century 

def fix_date(x):
    year = x.split('/')[2]
    if int(year) <= 19:
        return x[:-2] + '20' + year
    else:
        return x[:-2] + '19' + year

test.loc[test['release_date'].isnull()==True].head()
test.loc[test['release_date'].isnull()==True, 'release_date'] ='05/01/00'
train['realease_date'] =train['release_date'].apply(lambda x:fix_date(x))
test['realease_date'] =test['release_date'].apply(lambda x:fix_date(x))


# creating features based on Date

train['release_date'] = pd.to_datetime(train['release_date'])
test['release_date'] = pd.to_datetime(test['release_date'])

def process_date(df):
    date_parts = ['year','weekday','month','weekofyear','day','quarter']
    for part in date_parts:
        part_col = 'release_date' + '_' + part
        df[part_col] = getattr(df['release_date'].dt,part).astype(int)
    return df

train = process_date(train)
test = process_date(test)

# using plotly to visualize the number of films Per Year


d1 = train['release_date_year'].value_counts().sort_index()
d2 = test['release_date_year'].value_counts().sort_index()

data = [go.Scatter(x =d1.index, y=d1.values, name ='train'),
        go.Scatter(x =d2.index, y=d2.values, name ='test')]

layout = go.Layout(dict(title='Number of flims per year',
                        xaxis=dict(title='Year'),
                        yaxis=dict(title='Count'),
                        ),legend=dict(orientation='v'))
py.iplot(dict(data=data, layout=layout))


# Number of Flims and revenue per year 

d1 = train['release_date_year'].value_counts().sort_index()
d2 = train.groupby(['release_date_year'])['revenue'].sum()

data = [go.Scatter(x =d1.index, y=d1.values, name ='film count'),
        go.Scatter(x =d2.index, y=d2.values, name ='total revenue', yaxis='y2')]

layout = go.Layout(dict(title='Number of flims and total revenue per year',
                        xaxis=dict(title='Year'),
                        yaxis=dict(title='Count'),
                        yaxis2=dict(title='Total revenue', overlaying='y', side='right')),
                   legend= dict(orientation='v'))
py.iplot(dict(data=data, layout=layout))


d1 = train['release_date_year'].value_counts().sort_index()
d2 = train.groupby(['release_date_year'])['revenue'].mean()

data = [go.Scatter(x =d1.index, y=d1.values, name ='film count'),
        go.Scatter(x =d2.index, y=d2.values, name ='mean revenue', yaxis='y2')]

layout = go.Layout(dict(title='Number of flims and average revenue per year',
                        xaxis=dict(title='Year'),
                        yaxis=dict(title='Count'),
                        yaxis2=dict(title='average revenue', overlaying='y', side='right')),
                   legend= dict(orientation='v'))
py.iplot(dict(data=data, layout=layout))

# Dp release dates impact revenue 
sns.catplot(x = 'release_date_weekday' , y= 'revenue', data=train);
plt.title('Revenue of different days the week');


# Relationship btw Runtime and Revenue

sns.distplot(train['runtime'].fillna(0),bins=40, kde=False)
plt.title('Distribution of the length of film in hours')

sns.scatterplot(train['runtime'].fillna(0)/60, train['revenue'])
plt.title('runtime vs revenue')

