#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
  lengthOfSubarray  = len(arr[0])
  print(lengthOfSubarray)
  countPositive = 0
  countnegative = lengthOfSubarray - 1
  LtoR = 0
  RtoL = 0
  for x in arr:
    LtoR = LtoR + x[countPositive]
    RtoL = RtoL + x[countnegative]
    countPositive = countPositive + 1
    countnegative = countnegative - 1
  
  if LtoR >= RtoL:
    print(LtoR - RtoL)
  else:
     print(RtoL  - LtoR)

    

if True:
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()