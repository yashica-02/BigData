#Display upward closing price movement list, i.e. higher price than the previous highest so far (e.g. 1625, 1638, 1648, 1651, 1680, 1711, ...).

import sys

next(sys.stdin)
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    date=(line[0])
    cprise=float(line[5])
    
    print("%s\t%f" % (date, cprise))