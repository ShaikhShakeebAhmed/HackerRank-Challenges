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
    for i in range(len(arr)):
      print(arr[i])
      if arr[i] > arr[i-1] and i > 0 and arr[i] < totallen:
        test=True
      else:
        if arr[i] < totallen and i > 0 and arr[i-1] < arr[i]:
          print(arr[i])
          #arr[i] = arr[i-1] + 1
          #count += 1
          print(arr[i])
          print("- 1")
        elif arr[i] > totallen and i == 0:
          print(arr[i])
          arr[i] = 1
          count += 1
          print(arr[i])
          print("- 2")
        elif arr[i] > totallen and arr[i-1] < arr[i] and i > 0:
          print(arr[i])
          arr[i] = arr[i - 1] + 1
          count += 1
          print(arr[i])
          print("- 3")
        elif arr[i] < totallen and arr[i-1] >= arr[i] and i > 0:
          print(arr[i])
          arr[i] = arr[i - 1] + 1
          count += 1
          print(arr[i])
          print("- 4")

     

  print(arr)  
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

