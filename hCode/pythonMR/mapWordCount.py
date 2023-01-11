#find how many times a word has been repeated

import sys

# input comes from STDIN (Standard Input)
for line in sys.stdin:
    line = line.strip()  #remove leading and trailing whitespace
    words = line.split() #split the line into words
    for word in words:   #for each word
        #write the results to STDOUT (Standard Output)
        #what we output here will be the input for the reduce step
        
        print ('%s\t%s' % (word, 1))
        #tab-delimited; the trivial word count is 1
        #mapper is not computing word occurrences sum
        