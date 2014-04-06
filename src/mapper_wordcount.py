#!/usr/bin/python


# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    # remove leading and tailing whitespaces
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the result into STDOUT
        # what we output here will be the input for the
        # reducer step, i.e. the input for reducer.py
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

#import sys

#for line in sys.stdin:
#    data = line.strip().split("\t")
#    if len(data) == 6:
#        date, time, store, item, cost, payment = data
#        print "{0}\t{1}".format(store, cost)

