#!/usr/bin/env python
import sys, re

for line in sys.stdin:
    # remove non alpha-numeric
    line = re.sub("[^a-zA-Z0-9]", " ", line)

    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    words = line.split()

    # increase counters
    for word in words:
    	# tab delimited; this word happend one time
	# write the results to STDOUT (standard output);
	# what we output here will be the input for the
	# Reduce step, i.e. the input for reducer.py
	#
	# tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)

