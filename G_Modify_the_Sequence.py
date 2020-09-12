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
     # print(len(arr)-1)   
      for j in range(len(arr)): 
        #print("j is " , j)
        if j < len(arr)-1:
          if ((arr[j] < arr[j + 1] and arr[j] > arr[j - 1]) or (arr[j] > arr[j - 1]))  and j != 0:
            firstOftheSeq.append(arr[j])
            #firstOftheSeq.append(arr[j + 1])
           # print(arr[j])
            #print(j)
            #print("- 1")
          elif j == 0 and arr[j] < arr[j + 1]:
            firstOftheSeq.append(arr[j])
            #firstOftheSeq.append(arr[j + 1])
            #print(arr[j])
            #print(j)
            #print("- 2")
          elif j ==  len(arr)-1:
            firstOftheSeq.append(arr[j]) 
            #print(arr[j])
            #print(j)
            #print("- 3")         
          else :
            #print(j)
            #print("- 4") 
            if len(firstOftheSeq) > 0:
              collectionOfAllSequences[countSequence] = firstOftheSeq
              firstOftheSeq = []
              countSequence += 1  
          
            collectionOfAllSequences[countSequence] = [arr[j]]
            countSequence += 1 
            #collectionOfAllNonSequences.append(arr[j])
        elif arr[j] > arr[j - 1]:
          firstOftheSeq.append(arr[j])
          #firstOftheSeq.append(arr[j + 1])
          #print(arr[j])
          #print(j)
          #print("- 5")
          if len(firstOftheSeq) > 0:
              collectionOfAllSequences[countSequence] = firstOftheSeq
              firstOftheSeq = []
              countSequence += 1
          else:
            collectionOfAllSequences[countSequence] = [arr[j]]
            countSequence += 1

      print(collectionOfAllSequences)

      listOfKeys=[]
      listOfKeysOfSequences=[]
      countKeys = 0
      for k in collectionOfAllSequences.keys():
        if len(collectionOfAllSequences[k]) > 1:
          
          if len(listOfKeys) > 0:
            print("listOfKeys" , listOfKeys)
            keysReversed = listOfKeys[::-1]
            listOfKeys=[]
            print("reversed" , keysReversed)
            firstOfTheSequence = collectionOfAllSequences[k][0]
            print("firstOfTheSequence" , firstOfTheSequence)
            LastOfThePreviusSequence = collectionOfAllSequences[listOfKeysOfSequences[-1]][-1]
            print("LastOfThePreviusSequence" , LastOfThePreviusSequence)
            completeSequence = collectionOfAllSequences[k]
            print("completeSequence" , completeSequence)
            for i in keysReversed:
              lastValue = collectionOfAllSequences[i][0]
              countingSmallers = 0
              for x in completeSequence:
                if lastValue > x: 
                   countingSmallers += 1
                else:
                  if countingSmallers > 0:
                    collectionOfAllSequences[i] = [firstOfTheSequence - 1]

          listOfKeysOfSequences.append(k)

                 
              

        else:
          listOfKeys.append(k)

  
  #print(collectionOfAllSequences)
  #print(len(arr)-1)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

