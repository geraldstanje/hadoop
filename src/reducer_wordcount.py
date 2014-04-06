#!/usr/bin/python

import sys

current_word = None 
current_count = 0
word = None

# input comes from Stdin
for line in sys.stdin:
	line = line.strip()
	
	word, count = line.split('\t', 1)
	
	try:
		count = int(count)
	except ValueError:
		continue
	
	if current_word == word:
		current_count += count
	else:
		if current_word:
			print '%s\t%s' % (current_word, current_count)
		current_count = count
		current_word = word
		
if current_word == word:
	print '%s\t%s' % (current_word, current_count)
    
#salesTotal = 0
#oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

#for line in sys.stdin:
#    data_mapped = line.strip().split("\t")
#    if len(data_mapped) != 2:
#        # Something has gone wrong. Skip this line.
#        continue

#    thisKey, thisSale = data_mapped

#    if oldKey and oldKey != thisKey:
#        print oldKey, "\t", salesTotal
#        oldKey = thisKey;
#        salesTotal = 0

#    oldKey = thisKey
#    salesTotal += float(thisSale)

#if oldKey != None:
#    print oldKey, "\t", salesTotal

