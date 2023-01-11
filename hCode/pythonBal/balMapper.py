# find the average balance for each age

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    
    age = int(line[0])
    bal = int(line[1])
    
    print ("%s\t%d" % (age,bal))