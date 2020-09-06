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
  countSequence = 0
  firstOftheSeq = []
  startSequence = 1000000000 - totallen
  
  #arr = sorted(arr , reverse = True)
  if len(arr) > 1:
    for i in range(0 , len(arr)-1 , 1):
      print(arr[i])
      print("- 1")
      countSequence = 0 
      firstOftheSeq = []       
      for j in range(i , len(arr)-1 , 1):
        print(arr[j])
        print("- 2")
        if arr[j] < arr[j + 1]:
          if arr[j] < 1000000000 and arr[j + 1] < 1000000000:
            firstOftheSeq.append(arr[j])
            firstOftheSeq.append(arr[j + 1])
            countSequence += 1            
            print("- 3")
            print(countSequence)
          elif arr[j] >= 1000000000:
            
            firstOftheSeq.append(arr[j])
            firstOftheSeq.append(arr[j + 1])
            countSequence += 1            
            print("- 4")
            print(countSequence)
          elif arr[j] >= 1000000000:
            firstOftheSeq.append(arr[j])
            firstOftheSeq.append(arr[j + 1])
            countSequence += 1            
            print("- 5")
            print(countSequence)
        else:
          print(firstOftheSeq)  
          if countSequence > 0:
            if arr[j]
            arr[i] = arr[i + 1] + 1
            count += 1


 
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

