import os
import sys

#
# Complete the modifySequence function below.
#
def modifySequence(arr):

  count = 0  
  testcount = 0
  totallen = len(arr)
  count = totallen
  startSequence = 1000000000 - totallen
  
  #arr = sorted(arr , reverse = True)
  if len(arr) > 1:
    for i in range(0 , len(arr)-1 , 1):
      #print(i)
      if arr[i] <= arr[i + 1] or arr[i] == arr[i - 1] and arr[i] < 1000000000:
        count = count - 1
      elif arr[i] >= 1000000000:
        count = count - 1

  #print(arr)  
  return totallen - count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

