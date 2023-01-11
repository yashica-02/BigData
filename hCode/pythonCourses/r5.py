#To classify the number of courses in each category depending upon price
#    Range : less than or equal to 50$
#    Range : less than or equal to 100$ and greater than 50$
#    Range : less than or equal to 150$ and greater than 100$
#    Range : less than or equal to 200$ and greater than 150$
#    Range : greater than 200$

import sys

r1=0
r2=0
r3=0
r4=0
r5=0

for line in sys.stdin:
    line=line.strip()
    line = line.split ('\t')
    
    price=int(line[0])
    
    if(price <= 50):
        r1=r1+1
    elif (100 >= price > 50):
        r2=r2+1
    elif (150 >= price > 100):
        r3=r3+1
    elif (200 >= price > 150):
        r4=r4+1
    else:
        r5=r5+1
    
print("Number of courses in each range: \n")
print("Less than or equal to 50$: %d" % r1)
print("Less than or equal to 100$ and greater than 50$: %d" % r2)
print("Less than or equal to 150$ and greater than 100$: %d" % r3)
print("Less than or equal to 200$ and greater than 150$: %d" % r4)
print("Greater than 200$: %d" % r5)