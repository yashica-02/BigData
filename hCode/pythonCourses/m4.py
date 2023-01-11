#Display URL and duration for all the courses at Expert Level having duration more than 3 hours.

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            url = line[2]
            dur = float(line[9])
            level=line[8]
    
            print(("%s\t%f\t%s") % (url,dur,level))
    except:
        continue