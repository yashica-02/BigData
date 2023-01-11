import sys

country = None
cty = None

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    Country = line[0]
    count=0
        
    if country == cty:
        count += 1
    else:
        if country:
            print ('%s\t%s' % (country, count))
        
        count = 1
        country = cty
        
if country == cty:
    print ('%s\t%s' % (country, count))