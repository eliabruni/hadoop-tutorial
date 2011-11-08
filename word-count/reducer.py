#!/usr/bin/env python

import sys

word2count = {}

for line in sys.stdin:
    # remove whitespaces (leading and trailing)
    line = line.strip()

    # parse the mapper input
    word, count = line.split('\t', 1)

    # convert count from string to int
    try:
        count = int(count)
	word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        # count wasn't a numbe, so we 
	# (silently) discard the line
        pass

# sort the words lexigraphically 
sorted_word2count = word2count.items()
sorted_word2count.sort()

for word, count in sorted_word2count:
    print '%s\t%s' % (word, count)
