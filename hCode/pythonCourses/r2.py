#To identify the number of courses available for each subject.

import sys

courses = {}

for line in sys.stdin:
    line=line.strip()
    (sub,course) = line.split ('\t', 1)
    
    cnt= 1
    
    if sub in courses:
        courses [sub] = courses [sub]+ cnt
    else:
        courses [sub] = cnt

for sub in courses.keys ():
    print ("Subject: %s \t Courses available: %d" % (sub, courses [sub]))