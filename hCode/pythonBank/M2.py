#Find account balance of those who are over the age of 30, single and have taken a personal loan

import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    age=int(line[0])
    mstat=line[2]
    bal=int(line[5])
    ploan=line[7]
    
    print("%d\t%s\t%d\t%s" % (age,mstat,bal,ploan))