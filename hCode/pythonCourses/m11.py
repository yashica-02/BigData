#Find courses which have more duration than average duration of paid courses.

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            cid = line[0]
            dur = int(line[9])
            paid=line[3]
    
            print(("%s\t%d\t%s") % (cid,dur,paid))
    except:
        continue