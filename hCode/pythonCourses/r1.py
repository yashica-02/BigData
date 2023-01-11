#To find the number of courses which can be pursed for the subject ‘Web Development?

import sys
count = 0

for line in sys.stdin:
    line = line.strip()
    
    course, subject = line.split("\t")
        
    if (course == "Web Development"):
        count = count + 1 

print (count)