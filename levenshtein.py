#!/usr/bin/env python3

# Lab 16: Recursion
# Levenshtein Distance

global lev_cache
lev_cache = {}

def lev(word1, word2):
	if(word1==""):
		return len(word2)
	elif(word2==""):
		return len(word1)
	 ##take off last letter
	score =0
	if (word1[-1] ==  word2[-1]):
		score = 0
	else:
		score =1 
	#+1 to distance for replacing last letter


	sub1 = (word1, word2[:-1])
	if not sub1 in lev_cache:
		lev_cache[sub1] = lev(sub1[0], sub1[1])

	sub2 = (word1[:-1], word2)
	if not sub2 in lev_cache:
		lev_cache[sub2] = lev(sub2[0], sub2[1])

	
	sub3 = (word1[:-1], word2[:-1]) #whether or not this change adds to distance depends on score
	if not sub3 in lev_cache:
		lev_cache[sub3] = lev(sub3[0], sub3[1])

	distance = min([lev_cache[sub1]+1, lev_cache[sub2]+1, lev_cache[sub3]+score])

	return distance

print(lev("descartes", "me"))
