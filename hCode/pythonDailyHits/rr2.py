#Find out daily count of successful and unsuccessful visits

import sys

sv={}
uv={}

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    date=line[0]
    stat=line[1]

    if stat == 200:
        if date in sv:
            sv[date].append(stat)
        else:
            sv[date] = []
            sv[date].append(stat)
    else:
        if date in uv:
            uv[date].append(stat)
        else:
            uv[date] = []
            uv[date].append(stat)

for date in sv.keys ():
    print ("Date: %s\tSuccessful visits: %s \t Unsuccessful visits: %s'" % (date, len(sv[date])))        
