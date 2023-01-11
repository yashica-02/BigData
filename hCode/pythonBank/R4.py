#Find the average balance of workers for different job profiles

import sys

jobs={}

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    job=line[0]
    bal=int(line[1])
    
    if job in jobs:
        jobs[job].append(bal)
    else:
        jobs[job]=[]
        jobs[job].append(bal)

for job in jobs.keys():  
    avgBal=sum(jobs[job])/len(jobs[job])
    print ('%s\t%f' % (job, avgBal))