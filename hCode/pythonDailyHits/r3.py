#Find out which IP address has sent the most requests.

import sys

ipcnt = {}

for line in sys.stdin:
    line=line.strip()
    ip,cnt = line.split ('\t',1)
    
    if ip in ipcnt:
        ipcnt [ip] = ipcnt [ip] + 1
    else:
        ipcnt [ip] = cnt
    print(ipcnt)

v= list (ipcnt.values ())
k= list (ipcnt.keys ())

print ("IP address with most requests is: ", k[v.index (max (v))], "and count is: ", max (v))