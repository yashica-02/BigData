#Find account balance of those who have taken both housing loan and personal loan

import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    bal=int(line[0])
    hloan=line[1]
    ploan=line[2]
    
    if(hloan=="yes" and ploan=="yes"):
        print(bal)