#Find account balance of those who are over the age of 30, single and have taken a personal loan

import sys

for line in sys.stdin:
    line=line.strip()
    line=line.split("\t")
    
    age=int(line[0])
    mstat=line[1]
    bal=int(line[2])
    ploan=line[3]
    
    if(age>30 and mstat=="single" and ploan=="yes"):
        print(bal)