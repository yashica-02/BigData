#Find the average balance of workers for different job profiles

import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    job=line[1]
    bal=int(line[5])
    
    print("%s\t%d" % (job,bal))