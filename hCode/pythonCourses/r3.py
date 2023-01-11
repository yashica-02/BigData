#Display course ID and URL for all the free courses which have more than 50 lectures.

import sys

for line in sys.stdin:
    line=line.strip()
    line = line.split ('\t')
    
    id = line[0]
    url = line[1]
    paid=line[2]
    lect=int(line[3])
    
    if(paid =='FALSE'):
        if(lect > 50):
            print ("Course ID: %s \t URL: %s" % (id, url))