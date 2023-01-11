#Find average of all the subscribers for each subject.

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            sub = line[11]
            course = line[1]
    
            print(("%s\t%s") % (sub, course))
    except:
        continue