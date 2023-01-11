#Display URL and duration for all the courses at Expert Level having duration more than 3 hours.

import sys

for line in sys.stdin:
    line=line.strip()
    line = line.split ('\t')
    
    url = line[0]
    dur = float(line[1])
    level=line[2]
    
    if(level =='Expert Level'):
        if(dur > 3):
            print ("URL: %s \t Duration: %f" % (url,dur))