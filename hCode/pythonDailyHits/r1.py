#Get a daily count of visitors

import sys

dats={}

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    date=line[0]
    
    if date in dats:
        dats[date].append(date)
    else:
        dats[date] = []
        dats[date].append(date)

for date in dats.keys():
     print('%s\t%d' % (date,len(dats[date])))