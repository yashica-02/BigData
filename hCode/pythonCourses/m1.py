#To find the number of courses which can be pursed for the subject ‘Web Development?

import sys

next(sys.stdin)
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    try:
        if(len(line) - 1 == 11):
            subject = line[11]
            course = line[1]
    
            print(("%s\t%s") % (subject, course))
    except:
        continue