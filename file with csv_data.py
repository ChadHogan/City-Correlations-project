'''this file is interacting with an exported csv file from the data base that has also been sorted by population size'''
import csv
import numpy as np


varg = []

with open('pymon/city-data forgit.csv') as data:
    test = csv.reader(data)
    for tag in test:
        varg.append(tag)
        print(tag)


for tag in varg:
    print(tag[0])


def datacorr(csvdata):
    
    x1 = []
    y2 = []

    for nar in csvdata: 
        try:
            var = nar[9]
            tar = nar[2]
            x1.append(float(var))
            y2.append(float(tar))
        except:
            Exception
        print(nar[1])
    return x1[1:], y2[1:]

Svarg = datacorr(varg)
lx, ly = Svarg

r = np.corrcoef(lx, ly)
print(r)