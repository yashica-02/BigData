import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    Country = line[1]

    print("%s" % (Country))