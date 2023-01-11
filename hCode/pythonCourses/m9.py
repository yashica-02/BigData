#To display the URL of the course that has maximum number of review at beginner level.

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            url=line[2]
            rev=int(line[6])
            level=line[8]
    
            print(("%s\t%d\t%s") % (url, rev, level))
    except:
        continue