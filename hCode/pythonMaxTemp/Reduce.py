#find the maximum temperature for each year

import sys

year_temp={}

for line in sys.stdin:
    line = line.strip()
    year,temp = line.split('\t')
    
    if year in year_temp:
        year_temp[year].append(int(temp))
    else:
        year_temp[year] = []
        year_temp[year].append(int(temp))

for year in year_temp.keys():
    max_temp=max(year_temp[year])
    print('%s -> %s' % (year, max_temp))
