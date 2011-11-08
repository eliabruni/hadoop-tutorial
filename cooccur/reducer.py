#!/usr/bin/env python

import sys
from operator import itemgetter

cooccurs = {}

for line in sys.stdin:
    line = line.strip()
    word1, word2, count = line.split('\t')
    try:
        count = int(count)
	if word1 in cooccurs:
	    cooccurs[word1][word2] =   cooccurs[word1].get(word2, 0) + count
	else:
	    cooccurs[word1] = {word2: 1}
    except ValueError:
        pass


sorted_keys = cooccurs.keys()
sorted_keys.sort()

for word1 in sorted_keys:
    for word2, count in sorted(cooccurs[word1].iteritems(),  key=itemgetter(1), reverse=True):
       print '%s\t%s\t%s' % (word1, word2, count)

