#Find courses which have more duration than average duration of paid courses.

import sys

pcrs={}

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    
    cid = line[0]
    dur = int(line[1])
    paid= line[2]

    if (paid=="TRUE"):
        pcrs[cid]=[]
        pcrs[cid].append(int(dur))
    
    avgc=sum(pcrs[cid])*1.0/len(pcrs[cid])