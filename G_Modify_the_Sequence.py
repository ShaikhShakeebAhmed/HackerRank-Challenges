import os
import sys

#
# Complete the modifySequence function below.
#
def modifySequence(arr):
  count = 0  
  testcount = 0
  totallen = len(arr)
  startSequence = 1000000000 - totallen
  #arr = sorted(arr , reverse = True)
  #print(arr)
  for i in range(len(arr)-1):
    if arr[i] >= 1000000000:
      arr[i] = arr[i - 1]
      
    
  for i in range(len(arr)-1):
    if arr[i +  1] <= arr[i] :
      arr[i+1] = arr[i] + 1
      count += 1
    
    
    
    
   
      
        
      
  print(arr)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

