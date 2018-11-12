#!/usr/bin/env python

import os
import string
import datetime


def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates



lines =os.popen('git log --pretty=format:"%cn  %ai" --shortstat')

name=""
date=""
add=0
map={}

names={}
dates=[]
result={}

for line in lines:
    if len(line) == 0 or line == '\n':
        continue
    if string.find(line,'changed')==-1:
        line1 = line.split(' ')
        #print line1
        name=line1[0]
        if name == '\xe6\x9d\x8e\xe7\x82\xab\xe5\xbd\xac':
            continue
        names[name]=0
        date=line1[2]
        dates.append(date)
    else:
        if string.find(line,'insertion')==-1:
            continue
        line2 = line.split(' ')
        add=int(line2[4])
        old=0
        key=date+"_"+name
        if map.has_key(key):
            old=map[key]
        map[key]=old+add

print map 
dates.sort()
dateMin=dates[0]
dateMax=dates[-1]

dateAll=dateRange(dateMin,dateMax)
for i in range(len(dateAll)):
    date=dateAll[i]
    
    
    
    for name in names:
        key=date+"_"+name
        
        value=0
        if map.has_key(key):
            value=map[key]
            print value 
        old=0
        if i>0:
            oldKey=dateAll[i-1]+"_"+name
            old=result[oldKey]
            
        result[key]=old+value
        


list= result.keys()
list.sort()

fo = open("result.csv", "w")
fo.write( "name,type,value,date\n")
for one in list:
    value=result[one]
    dateAndName = one.split('_')
    date=dateAndName[0]
    name=dateAndName[1]
    
    fo.write( name+",,"+str(value)+","+date+"\n")
     



            
        
        
    
			
 