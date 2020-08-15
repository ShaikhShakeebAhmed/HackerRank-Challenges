#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
  totallength = len(arr)  
  totalzero = [temp for temp in arr if temp == 0]
  totalAboveZero = [temp for temp in arr if temp > 0]
  totalBelowZero = [temp for temp in arr if temp < 0]
 # print(totallength , totalzero , totalAboveZero , totalBelowZero)
  ratioOfZero = len(totalzero) / totallength
  ratioOfAboveZero = len(totalAboveZero) / totallength
  ratioOfBelowZero = len(totalBelowZero) / totallength
  print("{:.6f}".format(round(ratioOfAboveZero , 6))
    , '\n' , "{:.6f}".format(round(ratioOfBelowZero , 6)) 
    , '\n' ,"{:.6f}".format(round(ratioOfZero , 6)))


if True:
  n = int(input())

  arr = list(map(int, input().rstrip().split()))

  plusMinus(arr)
