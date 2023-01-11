#Find jobs and balances higher than blue-collar averages

import sys

jobs=[]
baln=[]

cnt=0
tbc=0
abc=0

for line in sys.stdin:
    line=line.strip()
    (job,balance)=line.split("\t")
    bal=float(balance)
    jobs.append(job)
    baln.append(bal)
    
    if(job=="blue-collar"):
        cnt=cnt+1
        tbc=tbc+bal

abc=tbc/cnt

print("The avg. for blue collar is: %f" %abc)

print("Now printing balances more than the above...")

for i in range(len(jobs)):
    if(baln[i]>abc):
        print(jobs[i],baln[i])