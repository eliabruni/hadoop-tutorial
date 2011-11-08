#!/usr/bin/env python

import sys, re

# size of the context window
window = 2

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove non alpha-numeric
    line = re.sub("[^a-zA-Z-0-9]", " ", line)

    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    words = line.split()

    
    # increase counters
    #i = 0
    #while i < len(words):
    #    word = words[i]
    #	
    #	j = i - window
    #	while j < i + window + 1:
    #	    if j == i or j < 0:
    #	        j += 1
    #	        continue
    #	    if j >= len(words):
    #	        break
    #	    pair = word + ' ' +  words[j]
    #	    print '%s\t%s' % (pair, 1)
    #	    j += 1
    #	i += 1   
   
    i = 0
    while i < len(words) - 1:
        pair = (words[i], words[i+1])
        pair = sorted(pair)
        print '%s\t%s' % (pair[0] + ' ' + pair[1], 1)
        i += 1
