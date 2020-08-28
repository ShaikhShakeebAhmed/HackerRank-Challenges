import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
  Desc = sorted(arr, reverse=True)
  Asc = sorted(arr, reverse=False)
  print(sum(Desc[0:4]) , sum(Asc[0:4]))
  

if True:
  miniMaxSum([1,3,5,7,9])