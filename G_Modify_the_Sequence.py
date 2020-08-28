import os
import sys

#
# Complete the modifySequence function below.
#
def modifySequence(arr):
  count = 0
  N=len(arr)
  for i in range(N-1):
    if arr[i+1] <= arr[i]:
      count = (count+1)
  print(count)



if True:
    result = modifySequence([1,2,2,3,4])
    print(result)

