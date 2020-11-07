import os
import sys


global maximum 
  
def _lis(arr , n ): 
  
    # to allow the access of global variable 
    global maximum 
  
    # Base Case 
    if n == 1 : 
        return 1
  
    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 1
  
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
  
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    maximum = max(maximum , maxEndingHere) 
  
    return maxEndingHere 
  
def lis(arr): 
  
    # to allow the access of global variable 
    global maximum 
    x=[]

    for i in range(0,len(arr)):
      if 0 < arr[i] and arr[i] <= 1000000000:
        if arr[i] - i > 0:
          x.append(arr[i] - i)
  
    # lenght of arr 
    n = len(x) 
  
    # maximum variable holds the result 
    maximum = 1
  
    # The function _lis() stores its result in maximum 
    _lis(arr , n) 
    
    print (len(arr) - maximum)
  
# Driver program to test the above function 
# arr = [7,8,9,10,1,2,3,4,5,6] 
# n = len(arr) 
# print ("Length of lis is ", lis(arr))
  

# #def modifySequence(arr):
#   L=[] 
#   x= []
#   for i in range(1,len(arr)):
#     if 0 < arr[i] and arr[i] <= 1000000000:
#       if arr[i] - i > 0:
#         x.append(arr[i] - i)
#   print(x)
#   for (k,v) in enumerate(x):
#     L.append(max([L[i] for (i,n) in enumerate(x[:k]) if n<v] or [[]], key=len) + [v])

#   print(enumerate(x))
#   print(L)  
#   print (len(arr) - len(max(L, key=len)))
 
  


if True:
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lis(arr)
    #result = modifySequence([1,2,2,3,4])
    #print(result)