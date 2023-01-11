#Display course ID and URL for all the free courses which have more than 50 lectures.

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
  
    try:
        if(len(line) - 1 == 11):
            id = line[0]
            url = line[2]
            paid=line[3]
            lect=int(line[7])
    
            print(("%s\t%s\t%s\t%d") % (id,url,paid,lect))
    except:
        continue