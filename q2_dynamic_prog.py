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

def matrix(seq1, seq2):
    seq1 = '-' + seq1
    seq2 = '-' + seq2
    mx = [['X']]
    for i in seq1:
        mx[0].append(i)
    
    l = len(mx[0]) - 1
    
    for i in seq2:
        a = [i] + [None] * l
        mx.append(a)

    return mx

def s(mx, j , i):
    options = dict()

    options['E'] = 0

    if(j > 1 and i > 1):
        options['D'] = match(mx[j][0], mx[0][i]) + mx[j - 1][i - 1]

    if(j > 1):
        options['U'] = mx[j - 1][i] - 2

    if(i > 1):
        options['L'] = mx[j][i - 1] - 2

    return options

def fill_matrix(mx, bmx):
    for j in range(1, len(mx)):
        row = mx[j]
        for i in range(1, len(row)):
            opts = s(mx, j, i)
            
            maximum = None
            path = None
            for e in opts.keys():
                if maximum == None or opts[e] > maximum:
                    maximum = opts[e]
                    path = e

            mx[j][i] = maximum
            bmx[j][i] = path

def max_value(mx):
    c = None
    a = None
    for j in range(1, len(mx)):
        row = mx[j]
        for i in range(1, len(row)):
            if a == None or row[i] > a:
                a = row[i]
                c = [j, i]
    return c

def backtrack(bmx, j, i):
    seq1 = ''
    seq2 = ''

    while bmx[j][i] != 'E':
        it = bmx[j][i]
        
        if(it == 'D'):
            seq1 = bmx[0][i] + seq1
            seq2 = bmx[j][0] + seq2
            j -= 1
            i -= 1
        elif(it == 'L'):
            seq1 = bmx[0][i] + seq1
            seq2 = '-' + seq2
            i -= 1
        elif(it == 'U'):
            seq2 = bmx[j][0] + seq2
            seq1 = '-' + seq1
            j -= 1

    return (seq1, seq2)

def print_matrix(mx):
    for i in mx:
        print(i)

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
# To work with the printing functions below the best local alignment should be called best_alignment and its score should be called best_score. 

score_matrix = matrix(seq1, seq2)
backtrack_matrix = matrix(seq1, seq2)
fill_matrix(score_matrix, backtrack_matrix)

#print_matrix(score_matrix)
#print('---')
#print_matrix(backtrack_matrix)


mx = max_value(score_matrix)
best_score = score_matrix[mx[0]][mx[1]]
#print(mx)
best_alignment = backtrack(backtrack_matrix, mx[0], mx[1])

#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

