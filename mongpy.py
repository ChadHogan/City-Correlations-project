from ast import GtE
from pymongo import MongoClient
import pymongo
import numpy as np

client = MongoClient('localhost', 27017 )

db = client['centre-for-cities'] 
'''get database'''

collection = db['city-data']
'''get collection'''

varg = collection.find({'Total population 2020': {'$gte':  500000}})

warg =collection.find({'Total population 2020': { '$lte': 500000}})
print('hello')

Svarg = varg.sort([('Total population 2020', pymongo.ASCENDING)]) # this is one why to sort out the information.

sorted_warg = warg.sort([('Total population 2020', pymongo.ASCENDING)])

Svarg1 = varg.sort([('Total population 2020', pymongo.ASCENDING), ('GVA per hour 2019', pymongo.DESCENDING)]) #can mix it upwith two sorts

err = varg.sort('Total jobs 2020', 1) # this is another way of doing it similar to compass...

Svarg2 = varg.sort([('Total population 2020', pymongo.ASCENDING)])#maybe this is only useable once

''' go by population, so largest at bootom perhaps, and then just get btoh values, gva per hour and knolwedge inustries and then se if correlation.'''

x = []
y = []
for tag in Svarg:
    var = tag['Private knowledge intensive business services jobs 2020 (%)']
    tar = tag['GVA per hour 2019 (£)']
    x.append(var)
    y.append(tar)
    print(tag['City'])

''' i have sorted it with pymongo making it quite easy , so can justt append files'''
'''
y = []

for tag in Svarg2:
    tar = tag['GVA per hour 2019 (£)']
    y.append(tar)
   
'''
r = np.corrcoef(x, y)
print(r)

a = []
b = []

for ted in sorted_warg:
    try:
        var = ted['Private knowledge intensive business services jobs 2020 (%)']
        tar = ted['GVA per hour 2019 (£)']
        a.append(var)
        b.append(tar)
    except:
         Exception
    print(ted['City'])

ra = np.corrcoef(a, b)

'''make a function it be easier so you dont have to repeat yourself,

i can see what you do class stuff so can then use debug console easily'''

def datacorr(mongodata):
    
    x1 = []
    y2 = []

    for nar in mongodata: #this implies were using mongo cursor object
        try:
            var = nar['Private knowledge intensive business services jobs 2020 (%)']
            tar = nar['GVA per hour 2019 (£)']
            x1.append(var)
            y2.append(tar)
        except:
            Exception
        print(nar['City'])
    return x1, y2



'''make a data cleaner class... maybe using pandas for a table???
then also make a sorted and corrlation class to work on data.'''

sorted_warg.rewind() # i forget that iterators after being done need to reqind or be assigned anew
arrrr = datacorr(sorted_warg)

print(arrrr)

'''unpacked the tuple returned'''
l1 = []
l2 = []

l1, l2 = arrrr

'''awesome'''

'''maybe class with four arguments the data x y and the collumn names you want to use
i.e

class mongc_correlate( x, y , x_title, y_title):
    
the titles have to be strings and x,y list of numbers'''
