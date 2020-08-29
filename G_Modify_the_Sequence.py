import os
import sys

#
# Complete the modifySequence function below.
#
def modifySequence(arr):
  count = 0
  #print(len(arr))
  #arr = sorted(arr , reverse=False)
  for i in range(len(arr)-1):
    #if arr[i-1] > arr[i] and arr[i] > 0 :
      #arr[i] = arr[i-1] + 1
      #count = count + 1
    if  arr[i + 1] < arr[i] and arr[i] > 0:
      arr[i + 1] = arr[i] + 1
      count = count + 1
    #elif arr[i+1] <= arr[i] :
      #arr[i+1] = arr[i+1] + 1
      #count = count + 1
    #elif arr[i+1] >= arr[i] and arr[i-1] == arr[i]:
      #arr[i+1] = arr[i+1] + 1
      #count = (count+2)
    #if arr[i+1] <= arr[i] and arr[i-1] < arr[i]:
      #arr[i+1] = arr[i+1] + 1
      #count = (count+1)
    #elif arr[i+1] <= arr[i] and arr[i-1] > arr[i]:
      #arr[i+1] = arr[i+1] + 1
      #count = (count+2)
    #elif arr[i+1] >= arr[i] and arr[i-1] == arr[i]:
      #arr[i+1] = arr[i+1] + 1
      #count = (count+2)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

