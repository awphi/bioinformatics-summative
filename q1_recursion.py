#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
def match(s1, s2):	
	if(s1 == '-' or s2 == '-'):
		return -4
	elif(s1 == 'A' and s2 == 'A'):
		return 3
	elif(s1 == 'C' and s2 == 'C'):
		return 2
	elif(s1 == 'G' and s2 == 'G'):
		return 1 
	elif(s1 == 'T' and s2 == 'T'):
		return 2

	return -3

def score(seq1, seq2):
	s = 0
	for i in range(len(seq1)):
		s += match(seq1[i], seq2[i])
	return s

def align(bank1, bank2, seq1, seq2, arr):
	#GENERATE POSSIBILITIES
	choices = []
	lb1 = len(bank1)
	lb2 = len(bank2)

	if(lb1 > 0):
		choices.append([bank1[-1], '-'])
	
	if(lb2 > 0):
		choices.append(['-', bank2[-1]])
	
	if(lb1 > 0 and lb2 > 0):
		choices.append([bank1[-1], bank2[-1]])

	#BASE CASE - NO POSSIBILITIES
	if(len(choices) == 0):
		arr.append([''.join(seq1), ''.join(seq2)])
		return arr

	#RECURSIVE CASE
	for choice in choices:
		s1 = seq1.copy()
		s2 = seq2.copy()
		s1.insert(0, choice[0])
		s2.insert(0, choice[1])

		b1 = bank1.copy()
		b2 = bank2.copy()

		if(choice[0] != '-'):
			b1 = b1[:-1]
		
		if(choice[1] != '-'):
			b2 = b2[:-1]

		arr = align(b1, b2, s1, s2, arr)

	return arr
# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Call any functions you need here, you can define them above.
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
# The number of alignments you have checked should be stored in a variable called num_alignments.

best_score = None
best_alignment = None

al = []
ss1 = list(seq1)
ss2 = list(seq2)
a1 = []
a2 = []

for i in align(ss1, ss2, a1, a2, []):
	al.append(i)

num_alignments = len(al)

for i in al:
	s = score(i[0], i[1])
	if(best_score == None or s > best_score):
		best_score = s
		best_alignment = i

#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Alignments generated: '+str(num_alignments))
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------
