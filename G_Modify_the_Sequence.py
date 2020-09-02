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
  if len(arr) > 1:
    for i in range(len(arr) -1):
      
      first = arr[i]
      second = arr[i + 1] if i < len(arr) -1 else 0
      third = arr[i + 2] if i < len(arr) -2 else 0

      if first >= second and second >= third and i < len(arr) -2:
        if first >= 1000000000 and second < 1000000000 and third < 1000000000:
          arr[i + 1] = first + 1
          arr[i + 2] =  arr[i + 1] + 1
        count += 2
      elif first >= second and second <= third  and i < len(arr) -2:
        if first < third:
          arr[i + 1] = arr[i + 2] - 1
          count += 1
        else:
          arr[i + 1] = first + 1
          arr[i + 2] =  arr[i + 1] + 1
          count += 2
      elif first <= second and second >= third  and i < len(arr) -2:
        if first < third:
          arr[i + 1] = arr[i + 2] - 1
          count += 1
        else:
          arr[i + 1] = first + 1
          arr[i + 2] =  arr[i + 1] + 1
          count += 2

  print(arr)  
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

