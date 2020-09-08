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
    #for i in range(0 , len(arr)-1 , 1):
      
      countSequence = 0 
      firstOftheSeq = []
      collectionOfAllSequences={} 
      collectionOfAllNonSequences = []      
      for j in range(0 , len(arr)-1 , 1):        
        if arr[j] < arr[j + 1] and j != len(arr)-1 and arr[j] > arr[j - 1] and j != 0:
          firstOftheSeq.append(arr[j])
          firstOftheSeq.append(arr[j + 1])
          #print(firstOftheSeq)
        elif j == 0 and arr[j] < arr[j + 1]:
          firstOftheSeq.append(arr[j])
          firstOftheSeq.append(arr[j + 1])
        elif j ==  len(arr)-1 and arr[j] > arr[j - 1]:
          firstOftheSeq.append(arr[j])          
        else :
          if len(firstOftheSeq) > 0:
            collectionOfAllSequences[countSequence] = firstOftheSeq
            firstOftheSeq = []
            countSequence += 1 
          
          collectionOfAllSequences[countSequence] = [arr[j]]
          countSequence += 1 
          #collectionOfAllNonSequences.append(arr[j])
      
      for k in collectionOfAllSequences.keys():
        if len(collectionOfAllSequences[k]) > 1:
          print(collectionOfAllSequences[k])
        else:
          print(" - 1")
          print(collectionOfAllSequences[k])
          collectionOfAllSequences[k+1] = [collectionOfAllSequences[k][0] + 1]
          print(collectionOfAllSequences[k + 1])
          print(" - 1")

  
  #print(collectionOfAllSequences)
  #print(len(arr)-1)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

