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
      countSequence = 0 
      firstOftheSeq = []       
      for j in range((i+1) , len(arr)-1 , 1):
        print(arr[j])
        print("- 2")
        if arr[j] < arr[j + 1] and arr[j] > arr[j - 1] and arr[j] < 1000000000 and arr[j + 1] < 1000000000:
          firstOftheSeq.append(arr[j])
          firstOftheSeq.append(arr[j + 1])
          countSequence += 1            
          print("- 3")
          #print(countSequence)
        elif arr[j] >= 1000000000:
          arr[j] = arr[j - 1] + 1
          count += 1
          firstOftheSeq.append(arr[j])
          #firstOftheSeq.append(arr[j + 1])
          countSequence += 1            
          print("- 4")
          #print(countSequence)        
        else:
          #print(firstOftheSeq)
          print("- 6")  
          if len(firstOftheSeq) > 0:
            if firstOftheSeq[len(firstOftheSeq) -1] >= arr[j]:
              print(arr[j])
              print(firstOftheSeq[len(firstOftheSeq) -1] + 1)
              arr[j] = firstOftheSeq[len(firstOftheSeq) -1] + 1
              firstOftheSeq.append(arr[j])
              count += 1
              i += len(firstOftheSeq) -1
              #print(firstOftheSeq)
              print("- 7")
          elif arr[j + 1] <= arr[j] and arr[j] > arr[j - 1]:
            if arr[j] > arr[j - 1]:
              arr[j + 1] = arr[j] + 1
              count += 1                
              print("- 8")
              i = j
          elif arr[j + 1] >= arr[j] and arr[j + 1] <= arr[j - 1]:
            if arr[j + 1] >= 1000000000:
              arr[j + 1] = arr[j] + 1
              count += 1                         
              print("- 5")
              #print(countSequence)
            else:
              arr[j] = arr[j - 1] + 1
              count += 1
              i = j
              print("- 9")
          elif arr[j + 1] >= arr[j] and arr[j] <= arr[j - 1] and arr[j - 1] < arr[j + 1]:
            if arr[j + 1] >= 1000000000:
              arr[j + 1] = arr[j] + 1
              count += 1                       
              print("- 15")
              #print(countSequence)
            else:
              arr[j] = arr[j - 1] + 1
              count += 1
              i = j
              print("- 10")
            
          elif arr[j + 1] >= arr[j] and arr[j] <= arr[j - 1] and arr[j - 1] > arr[j + 1]:
            arr[j] = arr[j + 1] - 1
            arr[j - 1] = arr[j] - 1
            count += 2
            i = j
            print("- 11")
      break
              


  print(arr)
  return count



if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    print(result)

