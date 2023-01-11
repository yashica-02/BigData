#To classify the number of courses in each category depending upon price
#    Range : less than or equal to 50$
#    Range : less than or equal to 100$ and greater than 50$
#    Range : less than or equal to 150$ and greater than 100$
#    Range : less than or equal to 200$ and greater than 150$
#    Range : greater than 200$

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            price = int(line[4])
    
            print(("%d") % (price))
    except:
        continue