# find the average balance for each age

import sys
age_bal = {}    #empty dictionary will be used to add age & balance pairs

for line in sys.stdin:
    line = line.strip()
    age, bal = line.split('\t')
    
    #if the current age value is already in the age_bal dict.
    if age in age_bal:
        #only append the bal to the same age value list,
        #already exists with some bal values from earlier loop iterations
        age_bal[age].append(int(bal))
        #print (age_bal)
    
    else:
        #new age: not in dict, so add the age an bal as a new list entry
        age_bal[age]=[]     #creates empty list inside the dict with key as age
        age_bal[age].append(int(bal))
        #print (age_bal)
        
for age in age_bal.keys():
    av_bal = sum(age_bal[age])/len(age_bal[age])
    print ('%s\t%f' % (age, av_bal))