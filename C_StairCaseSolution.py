import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
  for i in range(1, n + 1):
       print(' ' * (n - i) + '#' * i)
    #print("#" )
    
n = int(input())
staircase(n)


  
