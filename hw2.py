# Name: Kevin Kim.
# Evergreen Login: Kimkev08
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math
import hw2_test
###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

n = hw2_test.n
sum1 = 0
i = 1


while i <= n:
    sum1 = sum1 + i
    i = i + 1
print sum1


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"



for i in range (2, 11):
    print 1.0/i


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range (1, n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2


###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
factor = 1
for i in range (1, n+1):
    factor = factor * i
print "factor number", n, "via loop:", factor


###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

for j in range (1, 11):
    n = 11 - j
    factor = 1
    for i in range (1, n+1):
        factor = factor * i
    print "factor number", n, "via loop:", factor

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

sum2 = 1
for j in range (1, 11):
    n = 11 - j
    factor = 1
    for i in range (1, n+1):
        factor = factor * i
    sum2 = sum2 + 1.0/factor
print sum2
print "e for comparison", math.e

###
### Collaboration
###
#Cliff Randolph

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?

# not saving as myself but as cliff possibly cause its cliff's computer
#reading and hw. took me about 2 hour with cliff's assistance