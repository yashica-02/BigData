#Find the average balance of blue-collar divorced people

import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    job=line[1]
    mstat=line[2]
    bal=int(line[5])
    
    print("%s\t%s\t%s" % (job,mstat,bal))