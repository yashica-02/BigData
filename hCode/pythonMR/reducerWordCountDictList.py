#find how many times a word has been repeated using dictionary
#Before running this, try the samplelistDict.py program to understand the concept

import sys

words = {}  #Dictionary

for line in sys.stdin:
    line=line.strip()
    (word, count) = line.split ('\t', 1)
    
    count= int (count)
    
    if word in words:
        words [word] = words [word]+ count
    else:
        words [word] = count

#debugging - print (words)

for word in words.keys ():
    print ("%s\t%s" % (word, words [word]))

#convert dictionary into a list-values
v= list (words.values ())

#convert dictionary into a list - keys
k= list (words.keys ())

print ("Word with maximum occurrences is: ", k[v.index (max (v))], "and count is: ", max (v))
print ("Word with minimum occurrences is: ", k[v.index (min(v))], " and count is: ", min (v))