#Find jobs and balances higher than blue-collar averages

import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    job=line[1]
    balance=int(line[5])
    
    print("%s\t%d" % (job,balance))