#Find account balance of those who have taken both housing loan and personal loan

import sys
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    bal=int(line[5])
    hloan=line[6]
    ploan=line[7]
    
    print("%d\t%s\t%s" % (bal,hloan,ploan))