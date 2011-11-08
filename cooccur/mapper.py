#!/usr/bin/env python

import sys, re


window = 2
for line in sys.stdin:
    line = re.sub("[^a-zA-Z-0-9]", " ", line)
    line = line.strip().lower()
    words = line.split()
    i = 0
    while i < len(words):
        word = words[i]
	j = i - window
	while j < i + window + 1:
	    if j == i or j < 0:
	        j += 1
	        continue
	    if j >= len(words):
	        break
	    print '%s\t%s\t%s' % (pair[0], pair[1], 1)
	    j += 1
	i += 1    
        
    
