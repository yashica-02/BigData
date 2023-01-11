#find how many times a word has been repeated

import sys

cur_word = None
cur_count = 0
word = None

# input comes from STDIN (Standard Input)
for line in sys.stdin:
    line = line.strip()  #remove leading and trailing whitespace
    word, count = line.split('\t', 1) #parse the input from mapper.py
    
    try:
        count = int(count)
    except ValueError:
        #count was not a number, so silently ignore/discard this line
        continue
    
    if cur_word == word:
        cur_count += count
    else:
        if cur_word:
            print ('%s\t%s' % (cur_word, cur_count))
        
        cur_count = count
        cur_word = word
        
if cur_word == word:
    print ('%s\t%s' % (cur_word, cur_count))