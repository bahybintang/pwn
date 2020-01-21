#!/usr/bin/python
import sys

endState = sys.argv[1]
bits = sys.argv[2]

for i in xrange(bits):
    state = endState ^ 0xFFFFFFFFFFFFFFFF
    
