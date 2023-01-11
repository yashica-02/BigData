#Display date, opening price, and closing price if the closing price is more than the opening price.

import sys

next(sys.stdin)
for line in sys.stdin:
    line=line.strip()
    line=line.split(",")
    
    date=(line[0])
    oprice=float(line[6])
    cprise=float(line[7])
    
    print("%s\t%f\t%f" % (date, oprice, cprise))