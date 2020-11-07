import os
import sys


def modifySequence(arr):
  L=[] 
  x= []
  for i in range(1,len(arr)):
    if 0 < arr[i] and arr[i] <= 1000000000:
      if arr[i] - i > 0:
        x.append(arr[i] - i)

  for (k,v) in enumerate(x):
    L.append(max([L[i] for (i,n) in enumerate(x[:k]) if n<v] or [[]], key=len) + [v])

  print(L)  
  print (len(arr) - len(max(L, key=len)))
 
  


if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = modifySequence(arr)
    #result = modifySequence([1,2,2,3,4])
    #print(result)