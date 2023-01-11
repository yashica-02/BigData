#To find which years where any courses were published.

import sys

year_course={}

for line in sys.stdin:
    line = line.strip()
    course,date = line.split('\t')
    
    cyear = date.split('-')[0]
    
    if cyear in year_course:
        year_course[cyear].append(course)
    else:
        year_course[cyear] = []
        year_course[cyear].append(course)

for cyear in year_course:
    print(cyear)