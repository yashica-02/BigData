#To find which years where any courses were published.

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            course = line[1]
            date = line[10]
    
            print(("%s\t%s") % (course,date))
    except:
        continue