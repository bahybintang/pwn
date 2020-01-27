#!/usr/bin/python
import random

# 

def setup(seed):
	global state
	state = 0
	for i in xrange(16):
		cur = seed & 3
		seed >>= 2
		state = (state << 4) | ((state & 3) ^ cur)
		state |= cur << 2

def next(bits):
	global state

	ret = 0
	for i in xrange(bits):
		print "\nOuter loop ({})".format(i)
		ret <<= 1
		ret |= state & 1
		print "Init\t\t: " + bin(state)

		print "Operation\t: " + str(bin(state << 1)) + " ^ " + str(bin(state >> 61)) + "  (" + str(state << 1) + " ^ " + str(state >> 61) + ")"

		state = (state << 1) ^ (state >> 61)
		print "Hasil\t\t: " + bin(state) + "  ({})".format(state)

		# Balikin length ke 64 bit
		state &= 0xFFFFFFFFFFFFFFFF
		print "AND\t\t: " + bin(state) + "  ({})".format(state)

		# Flip bit
		state ^= 0xFFFFFFFFFFFFFFFF
		print "XOR\t\t: " + bin(state)

		print "\nInner loop"
		for j in xrange(0, 64, 4):
			cur = (state >> j) & 0xF
			cur = (cur >> 3) | ((cur >> 2) & 2) | ((cur << 3) & 8) | ((cur << 2) & 4)
			state ^= cur << j
			print bin(state)

	return ret

# setup((random.randrange(0x10000) << 16) | random.randrange(0x10000))
setup(2)
next(1)

# 
