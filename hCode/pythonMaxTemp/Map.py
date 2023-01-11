#find the maximum temperature for each year

import sys

for line in sys.stdin:
    line = line.strip()
    year = int(line.split('-')[0])
    temp = int(line.split(':')[1])
    
    print("%s\t%d" % (year,temp))