#To find which courses are the most and the least popular.

import sys

cid_sub={}

for line in sys.stdin:
    line=line.strip()
    cid, sub = line.split ('\t')
    
    if cid in cid_sub:
        cid_sub[cid].append(int(sub))
    else:
        cid_sub[cid] = []
        cid_sub[cid].append(int(sub))

    maxc = max(sub)
    minc = min(sub)
    for sub in cid_sub:
        if (sub==maxc):
            print("Courses with most Popularity:- %s" % cid)
        elif (sub==minc):
            print("Courses with least Popularity:- %s" % cid)