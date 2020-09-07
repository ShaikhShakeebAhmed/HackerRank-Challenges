import os
import sys

#
# Complete the modifySequence function below.
#
def modifySequence(arr):

  count = 0  
  testcount = 0
  totallen = len(arr)
  #count = totallen
  countSequence = 0
  firstOftheSeq = []
  startSequence = 1000000000 - totallen
  
  #arr = sorted(arr , reverse = True)
  if len(arr) > 1:
    for i in range(0 , len(arr)-1 , 1):
      print(arr[i])
      print("- 1")
      countSequence = 1 
      firstOftheSeq = []
      collectionOfAllSequences={}       
      for j in range((i+1) , len(arr)-1 , 1):        
        if arr[j] < arr[j + 1] and arr[j] > arr[j - 1]:
          firstOftheSeq.append(arr[j])
          firstOftheSeq.append(arr[j + 1])
        elif len(firstOftheSeq) >= 1:
          collectionOfAllSequences.append(firstOftheSeq) 
          firstOftheSeq = []
          countSequence += 1 


  print(collectionOfAllSequences)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

