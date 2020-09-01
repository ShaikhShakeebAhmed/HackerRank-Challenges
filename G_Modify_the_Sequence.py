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
  for i in range(len(arr) -1):
    if arr[i] < arr[i + 1]:
      doNothing = 1
      print(arr[i])
      print("- 1")
    else:
      if arr[i] == arr[i + 1]:
        print(arr[i])
        print(arr[i+1])
        if arr[i + 1] < 1000000000:
          arr[i + 1] = arr[i + 1] + 1
          count += 1
        else:
          arr[i] =  arr[i - 1] + 1
          arr[i + 1] = arr[i] + 1
          count += 2
        #arr[i + 1] = arr[i + 1] + 1
        
        print(arr[i])
        print("- 2")
      elif arr[i] > arr[i + 1]:
        print(arr[i])
        if arr[i + 1] < 1000000000:
          checkingVar = arr[i + 1] - 1
        else:
          checkingVar = arr[i - 1] + 1
        #count += 1
        if checkingVar == arr[i-1]:
          arr[i-1] = checkingVar - 1
          arr[i] = checkingVar
          arr[i+1] = checkingVar + 1
          count += 3
          print(arr[i])
          print("- 4")
        elif checkingVar < arr[i-1]:
          arr[i] = arr[i-1] + 1
          arr[i+1] = arr[i] + 1
          count += 2
          print(arr[i])
          print("- 5")
        else:
          arr[i] = checkingVar
          print(arr[i])
          print("- 3")       

  print(arr)  
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

