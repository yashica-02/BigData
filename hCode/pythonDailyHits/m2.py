#Find out daily count of successful and unsuccessful visits

import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    
    date=line[1][1:12]
    if (len(line[3])==3):      
        stat=int(line[3])
    print('%s\t%d' % (date,stat))