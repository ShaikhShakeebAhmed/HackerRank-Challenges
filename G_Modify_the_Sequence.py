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
    print(arr[i])
    print("- 0")
    if arr[i] < 1000000000:
      if arr[i + 1] <= arr[i] and arr[i] > arr[i - 1]:
        if arr[i] > arr[i - 1]:
          print(arr[i - 1])
          print(arr[i])
          print(arr[i + 1])
          #arr[i - 1] = arr[i] - 1 
          #arr[i] = arr[i] + 1
          arr[i + 1] = arr[i] + 1
          count += 1 
          print(arr[i])
          print("- 1")
        elif arr[i + 1] >= arr[i] and arr[i + 1] <= arr[i - 1]:
          print(arr[i])
          arr[i] = arr[i - 1] + 1
          count += 1
          print(arr[i])
          print("- 2")
      elif arr[i + 1] <= arr[i] and arr[i] <= arr[i - 1]:
        print(arr[i])
        arr[i] = arr[i - 1] + 1
        arr[i + 1] = arr[i] + 1
        count += 2
        testcount +=1
        print(arr[i])
        print("- 5")
      elif arr[i + 1] >= arr[i] and arr[i + 1] <= arr[i - 1]:
        print(arr[i])
        arr[i] = arr[i - 1] + 1
        count += 1 
        print(arr[i]) 
        print("- 3")
      elif arr[i + 1] >= arr[i] and arr[i - 1] >= arr[i]:
        if arr[i + 1] > arr[i - 1] :
          print(arr[i])
          arr[i] = arr[i - 1] + 1
          count += 1 
          print(arr[i]) 
          print("- 6") 
        elif arr[i + 1] < arr[i - 1] :
          print(arr[i])
          arr[i] = arr[i - 1] + 1
          arr[i + 1] = arr[i] + 1
          count += 1 
          print(arr[i]) 
          print("- 7")           
    elif arr[i] >= 1000000000:
      print(arr[i])
      arr[i] = arr[i - 1] + 1
      #count += 1 
      print(arr[i])
      print("- 4")

  print(arr)
  print(testcount)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

