import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
  for i in range(0 , n, 1):
    x = n - i
    print(" " * x , "#" * i)
    #print("#" )
    
n = int(input())
staircase(n)


  
