#Find out which IP address has sent the most requests.

import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    
    ip =line[0]
    cnt=1
    print('%s\t%d' % (ip,cnt))