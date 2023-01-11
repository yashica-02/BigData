#find the average age of each gender

import sys

gen_age = {}

#partitioner
for line in sys.stdin:
    line = line.strip()
    gen,age = line.split('\t')
    
    if gen in gen_age:
        gen_age[gen].append(int(age))
    else:
        gen_age[gen] = []
        gen_age[gen].append(int(age))

#reducer
for gen in gen_age.keys():
    avg_age=sum(gen_age[gen])*1.0/len(gen_age[gen])
    print('%s\t%s' % (gen, avg_age))