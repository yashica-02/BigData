#Find the average balance of blue-collar divorced people

import sys

total=0
cnt=0

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    job=line[0]
    mstat=line[1]
    bal=int(line[2])
    
    if(job=="blue-collar" and mstat=="divorced"):
        total += bal
        cnt = cnt+1

print("Total balance of divorced blue-collar workers is: %d" % total)
print("and the average is: %d" % int(total/cnt))

#using list
#
# import sys
# baln={}
# same for loop and list
# if loop statement: baln.append(bal)
# print(f'Average: (sum(baln)/len(baln))')