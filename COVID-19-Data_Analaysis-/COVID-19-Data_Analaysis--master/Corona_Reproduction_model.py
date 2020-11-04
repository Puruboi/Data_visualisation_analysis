# -*- coding: utf-8 -*-
"""Created on Fri Mar 27 12:31:22 2020
@author: Puruboi
"""
# If one person is infected with COVID-19 virus (Coronavirus)
#  Existing literature regarding SARS-CoV-2 and other coronaviruses 
#(e.g. MERS-CoV, SARS-CoV) suggest that the incubation period may range from 2–14 days.
#  "MIN" if a person meet 3 person per day 
# a person can infect X people in 2-14 days step index of 3 ( if he is not found and 
# isolated until 14 days)

a=1 # person infected
r=3 # on min he might meet 3 people per day 
for i in range(2,15,2):
    x=(round((a*(r**i)-1)//(r-1)))
    if(i==2):
        print("he would have infected {} people before being found and isolated on end of {}nd day ".format(x,i))
    
    else:
        print("he would have infected {} people before being found and isolated on end of {}th  day ".format(x,i))
print(x)
# on a average a person might infect X people 
y=x/14 # in 14 days 
print("on a average if the person is not found and  isolated in the incubation period of 2-14 days on a average he can infect '{}' people".format(round(y)))

# those Y people infected can infect XX people in their probation period 

a1=y
r=3 # each contact 3 people per day 
for i in range(2,15,2):
    x1=(round((a*(r**i)-1)//(r-1)))
    if(i==2):
        print("they would have infected {} people before being found and isolated on end of {}nd day ".format(x1,i))
    
    else:
        print("they would have infected {} people before being found and isolated on end of {}th  day ".format(x1,i))
print(x1)
y1=x/14 # in 14 days 
print("on a average if the person is not found and  isolated in the incubation period of 2-14 days on a average he can infect '{}' people".format(round(y1)))

# according to Center for Systems Science and Engineering (CSSE) at Johns Hopkins University
b=852 # now these are confriemd cases including deaths and recovered

#if these confirmed cases are found and isolated with delays as previous sample
r=3
for i in range(2,15,2):
    x3=(round((b*(r**i)-1)//(r-1)))
    if(i==2):
        print("they would have infected {} people before being found and isolated on end of {}nd day ".format(x3,i))
    
    else:
        print("they would have infected {} people before being found and isolated on end of {}th  day ".format(x3,i))
print(x3)
# on a average a person might infect X people 
y2=x3/14  # in 14 days 
print("on a average they might have infected '{}' people  before  found and  isolated in the incubation period of 2-14 days.".format(round(y2)))

