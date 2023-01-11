#Get a daily count of visitors

import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    
    date=line[1][1:12]       
    print('%s' % (date))