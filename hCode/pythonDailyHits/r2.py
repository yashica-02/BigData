#Find out daily count of successful and unsuccessful visits

import sys

sv={}
uv={}

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    date=line[0]
    stat=int(line[1])

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
print("SV LIST")
for x in sv.keys():
    print(x,"\t",len(sv[x]))
print("UV LIST")
for x in uv.keys():
    print(x,"\t",len(uv[x]))
    

        
