import sys
for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    
    if len(line) >=2:
        gen=line[1]
        age=line[2]
        
        print('%s\t%s' % (gen,age))