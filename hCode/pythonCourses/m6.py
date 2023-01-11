#To find which courses are the most and the least popular.

import sys

#next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    #try:
    if(len(line) - 1 == 11):
        cid = line[0]
        sub = int(line[5])
    
        print(("%s\t%d") % (cid,sub))
   # except:
     #   continue